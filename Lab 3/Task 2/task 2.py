import math


def alpha_beta(node,depth,alpha,beta,max_player):
    if depth==0:
        return node.value
    if max_player:
        max_value = -math.inf
        for child in node.child:
            value = alpha_beta(child, depth - 1, alpha, beta, False)
            max_value = max(max_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return max_value
    else:
        min_value = math.inf
        for child in node.child:
            value = alpha_beta(child, depth - 1, alpha, beta, True)
            min_value = min(min_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return min_value
class NodeClass:
    def __init__(self,val,child=[]):
        self.value=val
        self.child=child
def pacman_game(c):
    given_values=[3, 6, 2, 3, 7, 1, 2, 0]
    leafs=[]
    for val in given_values:
        leafs.append(NodeClass(val))
    level2=[]
    for i in range(0, len(leafs), 2):
        left_child = leafs[i]
        right_child = leafs[i + 1]
        level2.append(NodeClass(None, [left_child, right_child]))
    level1 = []
    for i in range(0, len(level2), 2):
        left_child = level2[i]
        right_child = level2[i + 1]
        level1.append(NodeClass(None, [left_child, right_child]))
    tree_root= NodeClass(None,level1)

    val_wo_magic=alpha_beta(tree_root,3,-math.inf,math.inf,True)
    LsubMax= max(given_values[:4])-c
    RsubMax=max(given_values[4:])-c
    if LsubMax>val_wo_magic and LsubMax-val_wo_magic>=RsubMax-val_wo_magic :

        print(f"The new minimax value is {LsubMax}. Pacman goes left and uses dark magic")
    elif RsubMax>val_wo_magic and LsubMax-val_wo_magic<=RsubMax-val_wo_magic:
        print(f"The new minimax value is {RsubMax}. Pacman goes right and uses dark magic")
    else:
        print(f"The minimax value is {val_wo_magic}. Pacman does not use dark magic")
pacman_game(int(input("Enter c :")))