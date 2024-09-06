import math


def ab_Game_algo(node,depth_of_the_tree,alpha,beta,max_player_flag):
    if depth_of_the_tree==0:
        return node.value
    if max_player_flag:
        maximum_value = -math.inf
        for i in node.child:
            value = ab_Game_algo(i, depth_of_the_tree - 1, alpha, beta, False)
            maximum_value = max(maximum_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return maximum_value
    else:
        minimum_value = math.inf
        for j in node.child:
            value = ab_Game_algo(j, depth_of_the_tree - 1, alpha, beta, True)
            minimum_value = min(minimum_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return minimum_value
class NodeClass:
    def __init__(self,value_of_node,child_node=[]):
        self.value=value_of_node
        self.child=child_node
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

    val_wo_magic=ab_Game_algo(tree_root,3,-math.inf,math.inf,True)
    #brings out the subtree max
    LsubMax= max(given_values[:4])-c
    RsubMax=max(given_values[4:])-c

    #decide pacman moves
    if LsubMax>val_wo_magic and LsubMax-val_wo_magic>=RsubMax-val_wo_magic :

        print(f"The new minimax value is {LsubMax}. Pacman goes left and uses dark magic")
    elif RsubMax>val_wo_magic and LsubMax-val_wo_magic<=RsubMax-val_wo_magic:
        print(f"The new minimax value is {RsubMax}. Pacman goes right and uses dark magic")
    else:
        print(f"The minimax value is {val_wo_magic}. Pacman does not use dark magic")
pacman_game(int(input("Enter c :")))