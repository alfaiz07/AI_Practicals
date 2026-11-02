# Tic-Tac-Toe using Minimax Algorithm

board = [" "] * 9

def minimax(board, is_max):
    if " " not in board:
        return 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"

            if check(board, "O"):
                board[i] = " "
                return 1 if is_max else -1

            score = minimax(board, not is_max)
            board[i] = " "

            if is_max:
                if score == 1:
                    return 1
            else:
                if score == -1:
                    return -1

    return 0

def check(b, p):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(b[a] == b[c] == b[d] == p
               for a, c, d in wins)

def best_move():
    best_score = -2
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

# Display board
def display():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])

# Game
while True:
    display()

    pos = int(input("Enter position (0-8): "))

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position!")
        continue

    board[pos] = "X"

    if check(board, "X"):
        display()
        print("You Win!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    move = best_move()
    board[move] = "O"

    if check(board, "O"):
        display()
        print("AI Wins!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break