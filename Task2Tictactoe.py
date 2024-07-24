import math
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, "O"):
        return -10 + depth, None
    if is_winner(board, "X"):
        return 10 - depth, None
    if not get_possible_moves(board):
        return 0, None

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "X"
            score, _ = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = " "
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = "O"
            score, _ = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = " "
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score, best_move

def ai_turn(board):
    _, move = minimax(board, 0, True, -math.inf, math.inf)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X" if random.choice([True, False]) else "O"
    
    while True:
        print_board(board)
        
        if current_player == "X":
            print("AI's turn:")
            move = ai_turn(board)
        else:
            print("Your turn. Enter row and column (0-2):")
            row, col = map(int, input().split())
            move = (row, col)
        
        if move and board[move[0]][move[1]] == " ":
            board[move[0]][move[1]] = current_player
        else:
            print("Invalid move. Try again.")
            continue
        
        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        
        if not get_possible_moves(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
