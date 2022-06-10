board = {"1": ["1", False, 2], "2": ["2", False, 2], "3": ["3", False, 2],
         "4": ["4", False, 2], "5": ["5", False, 2], "6": ["6", False, 2],
         "7": ["7", False, 2], "8": ["8", False, 2], "9": ["9", False, 2], }


def print_board(board):
    print(f"{board['1'][0]}|{board['2'][0]}|{board['3'][0]}")
    print("-+-+-")
    print(f"{board['4'][0]}|{board['5'][0]}|{board['6'][0]}")
    print("-+-+-")
    print(f"{board['7'][0]}|{board['8'][0]}|{board['9'][0]}")
    print("\n\n")


winning_patterns = ["111", "000"]
