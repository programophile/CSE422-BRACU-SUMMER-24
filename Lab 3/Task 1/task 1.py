import math
import random


def alpha_beta(node,depth,alpha,beta,maximizing_player):
    if depth==0:
        return node['value']
    if maximizing_player:
        max_val=-math.inf
        for child_node in node['child']:
            val= alpha_beta(child_node,depth-1,alpha,beta,False)
            max_val=max(max_val,val)
            alpha=max(max_val,alpha)
            if beta<=alpha:
                break
        return max_val
    else:
        min_value=math.inf
        for child_node in node['child']:
            val=alpha_beta(child_node,depth-1,alpha,beta,True)
            min_value=min(min_value,val)
            beta=min(min_value,beta)
            if beta<=alpha:
                break
        return min_value
def tree_create(depth):
    if depth==0:
        val=random.choice([-1,1])
        return {'value':val,'child':[]}
    child=[tree_create(depth-1),tree_create(depth-1)]
    return {'value':None,'child':child}
def game(player1=int(input()),depth=5):
    tree=tree_create(depth)
    round=0
    player=player1
    winner_arr=[None,None]
    alpha_inital=-math.inf
    beta_initial=math.inf
    for i in range(3):
        print(1)
        winner=alpha_beta(tree,5,alpha_inital,beta_initial,player)
        if winner==1:
            print("subzero")
        else:
            print("socrpian",winner)
        player=1-player1
game()