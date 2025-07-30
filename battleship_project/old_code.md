import config
def create_board():
    board = [['~' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for row in board:
        print(' '.join(row))
    return board
if __name__ == "__main__":
    WIDTH, HEIGHT = config.config_grid()
    SHIPS = config.config_ships()
    board = create_board(WIDTH, HEIGHT)
-------
def config_grid():
    while True:   
        width_input = input("Enter the grid's Width: ")
        height_input = input("Enter the grid's Height: ")
        
        if width_input.isdigit() and height_input.isdigit():
            
            WIDTH = int(width_input)
            HEIGHT = int(height_input)
            if 5 <= WIDTH <= 15 and 5 <= HEIGHT <= 15:
                return WIDTH, HEIGHT
            else:
                print("The expected number should be between 5 and 15 (included)")
        else:
            print("Invalid Input. Expected inputs should be numbers.")

def config_ships():
    SHIPS = {
        "Ti_Lascar": 2,
        "Al_Ahbdul": 3,
        "North_Tower": 3,
        "Gro_Lascar": 4,
    }
    assert len(SHIPS) == 4, "There should be a total number of 4 ships."
    return SHIPS

while True:
    WIDTH, HEIGHT = config_grid()
    ship_specs = config_ships()
