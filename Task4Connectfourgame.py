import random

def print_game_board():
    """Prints the game board."""
    print("\n   A   B   C   D   E   F   G")
    for x in range(rows):
        print(f"{x + 1}  ", end="")
        for y in range(columns):
            if game_board[x][y] == "R":
                print("🔴", end="  ")  # Red chip emoji
            elif game_board[x][y] == "B":
                print("🔵", end="  ")  # Blue chip emoji
            else:
                print(" ", end="  ")  # Empty space
        print()

# Possible letters (A-G) for user input
possible_letters = ["A", "B", "C", "D", "E", "F", "G"]

# Game board (2D array)
rows = 6
columns = 7
game_board = [[" " for _ in range(columns)] for _ in range(rows)]

# Function to modify the turn
def modify_turn(space_picked, turn):
    game_board[space_picked][col_index] = turn

# Turn counter
turn_counter = 0

# Define who starts
current_turn = "R"  # R for Red, B for Blue

def is_valid_move(col):
    """Checks if a column has space for a chip."""
    return game_board[0][col] == " "

def get_next_empty_row(col):
    """Finds the first empty row in a column."""
    for row in range(rows - 1, -1, -1):
        if game_board[row][col] == " ":
            return row
    return None

def check_win(turn):
    """Checks for a winning condition."""
    # Check horizontal, vertical, and diagonal wins
    for row in range(rows):
        for col in range(columns - 3):
            if all(game_board[row][col + i] == turn for i in range(4)):
                return True

    for col in range(columns):
        for row in range(rows - 3):
            if all(game_board[row + i][col] == turn for i in range(4)):
                return True

    for row in range(rows - 3):
        for col in range(columns - 3):
            if all(game_board[row + i][col + i] == turn for i in range(4)):
                return True

    for row in range(3, rows):
        for col in range(columns - 3):
            if all(game_board[row - i][col + i] == turn for i in range(4)):
                return True

    return False

def print_winner(turn):
    """Prints the winner message."""
    print(f"Congratulations! Player {turn} wins!")

# Main game loop
while True:
    print_game_board()

    while True:
        user_input = input(f"Player {current_turn}, choose a column (A-G): ").upper()
        if user_input in possible_letters:
            col_index = possible_letters.index(user_input)
            if is_valid_move(col_index):
                break
            else:
                print("Column is full. Please choose another.")
        else:
            print("Invalid input. Please enter a letter from A-G.")

    row_index = get_next_empty_row(col_index)
    if row_index is not None:
        modify_turn(row_index, current_turn)

        if check_win(current_turn):
            print_game_board()
            print_winner(current_turn)
            break  # Exit the game loop

        # Switch turns
        current_turn = "B" if current_turn == "R" else "R"
    else:
        print("The board is full! It's a tie.")
        break

# Print the game board after the loop
print_game_board()
