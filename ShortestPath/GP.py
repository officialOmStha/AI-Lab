import math

# Tic-Tac-Toe with Minimax AI
# Player vs AI
# AI uses Minimax Algorithm to choose the optimal move

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

# Minimax algorithm
def minimax(b, depth, is_maximizing):
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
                score = minimax(b, depth+1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth+1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI chooses the best move
def best_move(b):
    move = -1
    best_score = -math.inf
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(b, 0, False)
            b[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Choose player symbol and who goes first
player_symbol = input("Choose your symbol (X/O): ").upper()
while player_symbol not in ['X','O']:
    player_symbol = input("Invalid choice! Choose X or O: ").upper()
ai_symbol = 'O' if player_symbol == 'X' else 'X'

turn = input("Who goes first? (player/AI): ").lower()
while turn not in ['player','ai']:
    turn = input("Invalid choice! Who goes first? (player/AI): ").lower()

# Game Loop
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