from board import create_board, print_board, valid_shot_coord, cpu_shooting
from ships import deploy_fleet, shot_processing, prepare_fleet
from config import BOARD_SIZE, SHIP_SPECS

def main(): #setup/initialize game
    player_board = create_board()
    cpu_board = create_board()
    player_fleet = prepare_fleet()
    player_lookup = deploy_fleet(player_board, player_fleet, "You")
    cpu_fleet = prepare_fleet()
    cpu_lookup = deploy_fleet(cpu_board, cpu_fleet, "CPU")
    player_shots_taken = set()
    cpu_shots_taken = set()
    player_remaining = len(set(player_lookup.values()))
    cpu_remaining = len(set(cpu_lookup.values()))

    while player_remaining > 0 and cpu_remaining > 0:
        print("\nYour board:")
        print_board(player_board)
        print("\nCPU's board:")
        print_board(cpu_board, hiding=True)
        shot = valid_shot_coord()
        if shot in player_shots_taken:
            print("You already shot there! Try again.")
            continue
        player_shots_taken.add(shot)
        result = shot_processing(shot, cpu_board, cpu_lookup)
        if result == "Sunk":
            cpu_remaining -= 1
        if cpu_remaining == 0:
            print("You won!")
            break
        cpu_shot = cpu_shooting()
        print(f"CPU fired at {chr(65 + cpu_shot[0])}{cpu_shot[1] + 1}")
        result = shot_processing(cpu_shot, player_board, player_lookup)
        if result == "Sunk":
            player_remaining -= 1
        if player_remaining == 0:
            print("You lose...")
            break

    print("Game over!")

if __name__ == "__main__":
    main()
