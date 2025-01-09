def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by space: ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue
        
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = current_player
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell is already occupied. Try again.")
        else:
            print("Invalid move. Row and column must be 0, 1, or 2.")

if __name__ == "__main__":
    tic_tac_toe()
