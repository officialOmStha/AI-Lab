import math

# Tic-Tac-Toe with Minimax + Alpha-Beta Pruning AI
# Player vs AI

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board(b):
    print(f"{b[0]}|{b[1]}|{b[2]}")
    print("-+-+-")
    print(f"{b[3]}|{b[4]}|{b[5]}")
    print("-+-+-")
    print(f"{b[6]}|{b[7]}|{b[8]}")
    print()

# Check for winner
def is_winner(b, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i]==player for i in wc) for wc in win_conditions)

# Check if board is full
def is_full(b):
    return ' ' not in b

# Minimax algorithm with Alpha-Beta Pruning
def minimax(b, is_maximizing, alpha, beta):
    if is_winner(b, 'O'):
        return 1
    if is_winner(b, 'X'):
        return -1
    if is_full(b):
        return 0

    if is_maximizing:
        max_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, False, alpha, beta)
                b[i] = ' '
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # prune remaining branches
        return max_score
    else:
        min_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, True, alpha, beta)
                b[i] = ' '
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # prune remaining branches
        return min_score

# AI chooses the best move
def best_move(b):
    move = -1
    best_score = -math.inf
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(b, False, -math.inf, math.inf)
            b[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Let the player choose symbol and who goes first
player_symbol = input("Choose your symbol (X/O): ").upper()
while player_symbol not in ['X','O']:
    player_symbol = input("Invalid choice! Choose X or O: ").upper()
ai_symbol = 'O' if player_symbol == 'X' else 'X'

turn = input("Who goes first? (player/AI): ").lower()
while turn not in ['player','ai']:
    turn = input("Invalid choice! Who goes first? (player/AI): ").lower()

# Game loop
while True:
    print_board(board)

    if turn == 'player':
        # Player move
        while True:
            try:
                player_move = int(input("Enter your move (0-8): "))
                if board[player_move] == ' ':
                    board[player_move] = player_symbol
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter a number from 0 to 8.")
        turn = 'ai'
    else:
        # AI move
        ai_move = best_move(board)
        board[ai_move] = ai_symbol
        print(f"AI chose: {ai_move}")
        turn = 'player'

    # Check for winner
    if is_winner(board, player_symbol):
        print_board(board)
        print("You win!")
        break
    if is_winner(board, ai_symbol):
        print_board(board)
        print("AI wins!")
        break
    if is_full(board):
        print_board(board)
        print("Tie!")
        break