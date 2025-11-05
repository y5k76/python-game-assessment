# Tic Tac Toe Game (2 Players)

# Function to display the board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

print("🎮 Welcome to Tic Tac Toe! 🎮")
player1 = input("Enter Player 1 name (X): ")
player2 = input("Enter Player 2 name (O): ")

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
current_player = player1
current_mark = "X"

game_on = True

while game_on:
    display_board(board)
    choice = input(f"{current_player} ({current_mark}), choose a position (1-9): ")

    if choice not in board:
        print("❌ Invalid move. Try again.")
        continue

    board[int(choice) - 1] = current_mark

    # Check for a winner
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            display_board(board)
            print(f"🏆 {current_player} wins! Congratulations!")
            game_on = False
            break

    if game_on and all(s in ["X", "O"] for s in board):
        display_board(board)
        print("🤝 It's a draw!")
        game_on = False

    if current_player == player1:
        current_player = player2
        current_mark = "O"
    else:
        current_player = player1
        current_mark = "X"
