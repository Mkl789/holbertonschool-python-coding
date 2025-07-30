from config import BOARD_SIZE
def create_board():
    row_len = ['~'] * BOARD_SIZE
    board = [list(row_len) for _ in range(BOARD_SIZE)]
    return board
    print(board)
create_board()