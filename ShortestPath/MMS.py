import math

# Simple Tic-Tac-Toe board
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

def minimax(b, is_maximizing):
    if is_winner(b, 'O'):
        return 1
    if is_winner(b, 'X'):
        return -1
    if is_full(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(b):
    move = -1
    best_score = -math.inf
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(b, False)
            b[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Game Loop
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