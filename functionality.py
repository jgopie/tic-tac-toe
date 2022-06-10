from game_board import board, winning_patterns
import random


def validate_move(user_move):
    if user_move in board.keys() and not board[user_move][1]:
        board[user_move][2] = 0
        board[user_move][1] = True
        board[user_move][0] = "X"
    else:
        user_move = input("That move is invalid. Please make another move: ")
        validate_move(user_move)


def make_pc_move():
    move = str(random.randint(1, 9))
    if board[move][1]:
        make_pc_move()
    else:
        board[move][2] = 1
        board[move][1] = True
        board[move][0] = "O"


def check_winner():
    pattern = ''.join([str(values[2]) for values in board.values()])
    if pattern[0:3] in winning_patterns:
        return [True, board["1"][0]]
    if pattern[0::3] in winning_patterns:
        return [True, board["1"][0]]
    if pattern[0::4] in winning_patterns:
        return [True, board["1"][0]]
    if pattern[1::3] in winning_patterns:
        return [True, board["2"][0]]
    if pattern[2::3] in winning_patterns:
        return [True, board["3"][0]]
    if pattern[2::2] in winning_patterns:
        return [True, board["3"][0]]
    if pattern[3:5] in winning_patterns:
        return [True, board["4"][0]]
    if pattern[6:8] in winning_patterns:
        return [True, board["7"][0]]
    else:
        return[False, 0]
