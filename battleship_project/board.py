from config import BOARD_SIZE

previous_shots = set()

def valid_shot_coord():
    while True:
        user_input = input("Enter shot coordinates (row letter and column number, no space): ").strip().upper()
        if len(user_input) < 2: #invalid input
            print("Invalid Input. Have you entered more or less than two characters? Try again.")
            continue
        row_label = user_input[0] #slicing to take either the first char (letter=row) or second (number=col)
        col_header = user_input[1:]
        if not row_label.isalpha() or not col_header.isdigit(): #invalid input
            print("Have you correctly entered the coordinates (e.g. A1)? Try again.")
            continue
        row_index = ord(row_label) - ord("A")
        col_index = int(col_header) - 1
        if not (0 <= row_index < BOARD_SIZE) or not (0 <= col_index < BOARD_SIZE): #invalid input
            print("Coordinates out of bounds (range: A-E, 1-5)! Try again.")
            continue
        if (row_index, col_index) in previous_shots: #already shot there
            print("You already shot there! Try again.")
            continue
        
        return (row_index, col_index)

def create_board():
    row_len = ['~'] * BOARD_SIZE
    board = [list(row_len) for _ in range(BOARD_SIZE)]
    return board

def print_headers():
    print(" ", end="")
    for col in range(1, BOARD_SIZE + 1):
        print(col, end=" ")
    print()
    
def print_board(board, hiding=False):
    print_headers()
    for i in range(BOARD_SIZE):
        rows = []
        for cell in board[i]:
            if hiding and cell == "S":
                rows.append("~")
            else:
                rows.append(cell)
        print(chr(65 + i), * board[i])

def run_game(): #to run the game but created it for the revious shots check to work
    board = create_board()
    print_board(board)

    while True:
        shot = valid_shot_coord()
        previous_shots.add(shot)
        print(f"You fired at {chr(65 + shot[0])}{shot[1] + 1}")

if __name__ == "__main__":
    run_game()
