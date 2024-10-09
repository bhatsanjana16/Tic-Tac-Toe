import math

# Constants for the game
HUMAN = 'X'
AI = 'O'
EMPTY = '_'

# Initialize the Tic-Tac-Toe board
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


# Check if a player has won the game
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all([spot != EMPTY for row in board for spot in row])


# Minimax algorithm to find the best move for AI
def minimax(board, depth, is_maximizing):
    # Check terminal states
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:  # AI's turn (Maximizing player)
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = AI
                    score = minimax(board, depth + 1, False)
                    board[r][c] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:  # Human's turn (Minimizing player)
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[r][c] = EMPTY
                    best_score = min(score, best_score)
        return best_score


# Function to find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = AI
                score = minimax(board, 0, False)
                board[r][c] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (r, c)
    return move


# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's move
        row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        if board[row][col] == EMPTY:
            board[row][col] = HUMAN
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)

        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI's move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = AI
            print("AI plays:")
            print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
