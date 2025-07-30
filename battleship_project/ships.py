from config import SHIP_SPECS, BOARD_SIZE
import random

class Ship:
    def __init__(self, length, name=None):
        self.length = length
        self.positions = []
        self.hits = set()
        self.name = name
        
    def occupied_positions(self, positions):
        self.positions = positions

    def hit_tracking(self, coordonates):
        if coordonates in self.positions:
            self.hits.add(coordonates)

    def sunken(self):
        
        return set(self.positions) == self.hits

def prepare_fleet():
    names = ["North Tower", "Ti Lascar", "Gro Lascar", "Al Ahbdul"]
    fleet = []
    
    for i in range(SHIP_SPECS):
        fleet.append(Ship(SHIP_SPECS[1], names[1]))
        
    return fleet 

def random_ship_positioning(board, Ship):
    orientation = random.choice(["H", "V"])
    placed_ship = False
    while not placed_ship:
        if orientation == "H":
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, (BOARD_SIZE - Ship.length)) #BOARD_SIZE - Ship.length => in bounds
        else:
            row = random.randint(0, (BOARD_SIZE - Ship.length))
            col = random.randint(0, BOARD_SIZE - 1)
        positions = []
        for i in range(Ship.length):
            if orientation == "H":
                positions.append((row, col + i)) #memo as to how it builds: len=3, direct=H, start.point(2, 1) => i=0 -> (2, 1), i=1 -> (2, 2), i=2 -> (2, 3). Pos = [(2.1), (2,2), (2,3)] = Ship!
            else:
                positions.append((row + i, col))
        valid_position = True #checks if position is valid (no overlapping and/or out of bounds)
        for r, c in positions:
            if board[r][c] != '~':
                valid_position = False
                break
            else:
                for r, c in positions:
                    board[r][c] = "S"
                Ship.positions = positions #(so it saves to Ship object)
                placed_ship = True
        
def deploy_fleet(board, fleet, owner="CPU"): #returns a coord to ship map for hit detection andnaccept owner label (cpu)
    lookup = {}
    for Ship in fleet:
        random_ship_positioning(board, Ship)
        for pos in Ship.positions:
            lookup[pos] = Ship
    
    return lookup 
