# Alpha-Beta Pruning

def alphabeta(depth, node, maximizing, values, alpha, beta):

    if depth == 3:
        return values[node]

    if maximizing:
        best = -999

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              False, values, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alphabeta(0, 0, True, values, -999, 999)

print("Optimal Value:", result)