from game_board import print_board, board
from functionality import validate_move, make_pc_move, check_winner
import time

print_board(board)
game_over = [False, 0]

while not game_over[0]:
    user_move = input("Your move. Enter a number to claim that space: ")
    validate_move(user_move)
    print_board(board)
    game_over = check_winner()
    if game_over[0]:
        break
    time.sleep(1)
    make_pc_move()
    print_board(board)
    game_over = check_winner()

if game_over[1] == "X":
    print("Congratulations! You won!")
else:
    print("Better luck next time!")
