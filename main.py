#packman
def minimax_with_alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

class PacmanGameTreeNode:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def pacman_game(c):
    # Create the tree structure
    leaf_values = [3, 6, 2, 3, 7, 1, 2, 0]
    leaves = [PacmanGameTreeNode(value) for value in leaf_values]

    level2 = [PacmanGameTreeNode(None, [leaves[i], leaves[i+1]]) for i in range(0, len(leaves), 2)]
    level1 = [PacmanGameTreeNode(None, [level2[i], level2[i+1]]) for i in range(0, len(level2), 2)]
    root = PacmanGameTreeNode(None, level1)

    # Alpha-beta pruning without dark magic
    root_value_without_magic = minimax_with_alpha_beta(root, 3, float('-inf'), float('inf'), True)
    #print(f"Final value of the root node without using dark magic: {root_value_without_magic}")

    # Determine if using dark magic is beneficial
    left_subtree_max = max(leaf_values[:4]) - c
    right_subtree_max = max(leaf_values[4:]) - c

    if left_subtree_max > root_value_without_magic or right_subtree_max > root_value_without_magic:
        if left_subtree_max > right_subtree_max:
            print(f"The new minimax value is {left_subtree_max}. Pacman goes left and uses dark magic")
        else:
            print(f"The new minimax value is {right_subtree_max}. Pacman goes right and uses dark magic")
    else:
        print(f"The minimax value is {root_value_without_magic}. Pacman does not use dark magic")

# Sample Input
c = 5
pacman_game(c)

c = 3
pacman_game(c)
