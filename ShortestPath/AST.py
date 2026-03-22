import math

# Board setup
board = [' ' for _ in range(9)]

def print_board(b):
    print(f"{b[0]}|{b[1]}|{b[2]}")
    print("-+-+-")
    print(f"{b[3]}|{b[4]}|{b[5]}")
    print("-+-+-")
    print(f"{b[6]}|{b[7]}|{b[8]}")
    print()

def is_winner(b, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i]==player for i in wc) for wc in win_conditions)

def is_full(b):
    return ' ' not in b

# Minimax with Alpha-Beta
def minimax(b, depth, is_maximizing, alpha, beta):
    if is_winner(b, 'O'):
        return 10 - depth
    if is_winner(b, 'X'):
        return depth - 10
    if is_full(b):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                eval = minimax(b, depth+1, False, alpha, beta)
                b[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # prune
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                eval = minimax(b, depth+1, True, alpha, beta)
                b[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # prune
        return min_eval

def best_move(b):
    move = -1
    best_score = -math.inf
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(b, 0, False, -math.inf, math.inf)
            b[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
while True:
    print_board(board)
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == ' ':
        board[player_move] = 'X'
    else:
        print("Invalid move!")
        continue

    if is_winner(board, 'X'):
        print_board(board)
        print("You win!")
        break
    if is_full(board):
        print_board(board)
        print("Tie!")
        break

    ai_move = best_move(board)
    board[ai_move] = 'O'
    print(f"AI chose: {ai_move}")

    if is_winner(board, 'O'):
        print_board(board)
        print("AI wins!")
        break
    if is_full(board):
        print_board(board)
        print("Tie!")
        break