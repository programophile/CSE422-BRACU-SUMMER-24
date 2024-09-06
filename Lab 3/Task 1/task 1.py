import math
import random
def AB_algo(depth, node_index, maximizer, leaf_tree, alpha, beta):
    if depth == 5:
        return leaf_tree[node_index]

    if maximizer:
        maximum_value = -math.inf
        for iteration in range(2):
            maximized =AB_algo(depth + 1, node_index * 2 + iteration, False, leaf_tree, alpha, beta)
            maximum_value = max(maximum_value, maximized)
            alpha = max(alpha, maximized)
            if beta <= alpha:
                break
        return maximum_value
    else:
        minimum_value = math.inf
        for iteration in range(2):
            minimized = AB_algo(depth + 1, node_index * 2 + iteration, True, leaf_tree, alpha, beta)
            minimum_value = min(minimum_value, minimized)
            beta = min(beta, minimized)
            if beta <= alpha:
                break
        return minimum_value


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
    for _ in range(3):
        game_tree = []
        for _ in range(2 ** depth):
            value = random.choice([-1, 1])
            game_tree.append(value)
        # print(1)
        if player==1:
            winnin_player=AB_algo(depth,0,player,game_tree,alpha_inital,beta_initial)

        elif player==0:
            winnin_player = AB_algo(depth, 0, player, game_tree, alpha_inital, beta_initial)

        if winnin_player==1:
            round_winner_arr.append("subzero")
            winner_arr[1] += 1

        elif winnin_player==-1:
            round_winner_arr.append("socrpian")
            winner_arr[0] += 1

        # print(round_winner_arr)
        player= not player
        # print(player)
    # print(winner_arr)
    if winner_arr[0]>winner_arr[1]:
        print("Game winner: Sorpion")
    else:
        print("Game winner: Subzero")
    print(f"Total rounds played: {winner_arr[0]+winner_arr[1]}")
    for i in range(3):
        print(f"Winner of Round {i}: {round_winner_arr[i]}")

game()