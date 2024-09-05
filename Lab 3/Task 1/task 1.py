import math
import random
def alpha_beta(depth, node_index, maximizer, leaf_tree, alpha, beta):
    if depth == 5:
        return leaf_tree[node_index]

    if maximizer:
        max_eval = float('-inf')
        for i in range(2):
            A_chk =alpha_beta(depth + 1, node_index * 2 + i, False, leaf_tree, alpha, beta)
            max_eval = max(max_eval, A_chk)
            alpha = max(alpha, A_chk)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            B_chk = alpha_beta(depth + 1, node_index * 2 + i, True, leaf_tree, alpha, beta)
            min_eval = min(min_eval, B_chk)
            beta = min(beta, B_chk)
            if beta <= alpha:
                break
        return min_eval


def game(player1=int(input("Enter player no:")),depth=5):


    # print(tree)
    round=0
    if player1==1:

        player=True
    else:
        player=False
    # player=player1
    winner_arr=[0,0]
    round_winner_arr=[]
    alpha_inital=-math.inf
    beta_initial=math.inf
    for i in range(3):
        tree = [random.choice([-1, 1]) for _ in range(2 ** depth)]
        # print(1)
        if player==1:
            round_winner=alpha_beta(depth,0,player,tree,alpha_inital,beta_initial)

        elif player==0:
            round_winner = alpha_beta(depth, 0, player, tree, alpha_inital, beta_initial)

        if round_winner==1:
            round_winner_arr.append("subzero")
            winner_arr[1] += 1

        elif round_winner==-1:
            round_winner_arr.append("socrpian")
            winner_arr[0] += 1

        # print(round_winner_arr)
        player= not player
        # print(player)
    print(winner_arr)
    if winner_arr[0]>winner_arr[1]:
        print("Game winner: Sorpion")
    else:
        print("Game winner: Subzero")
    print(f"Total rounds played: {winner_arr[0]+winner_arr[1]}")
    for i in range(3):
        print(f"Winner of Round {i}: {round_winner_arr[i]}")

game()