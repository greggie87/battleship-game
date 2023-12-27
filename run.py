from random import randrange
import random

# Title
print("\nSOLO BATTLESHIP GAME!\n")
# Description and instructions
print("Guess where to shoot in order to sink the computer ships!\n")
print("There are 5 ships to sink with sizes of 5,4,3,2 and 1.")
print("X is a miss, O is a hit.")
print("@ means that you have sunk that ship completely.")
print("Aim to shoot by choosing a number on the grid from 0-99.\n")


# Game
def check_ok(boat, taken):
    """
    Checks boat is fully on the board
    """
    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat)-1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break

    return boat


def check_boat(b, start, dirn, taken):
    """
    Checks boat direction
    """
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_ok(boat, taken)
    return boat


def create_boats(taken, boats):
    """
    Creates the boats for the game board at random.
    Does not allow the ships to be generated off the board.
    Does not allow the ships to be generated into the same
    cell of the game board grid.
    """
    ships = []
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_boat(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat

    return ships, taken


def show_board(hit, miss, comp):
    """
    Game board area
    """
    print("\n     0  1  2  3  4  5  6  7  8  9\n")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " - "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " O "
            elif place in comp:
                ch = " @ "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def check_shot(shot, ships, hit, miss, comp):
    """
    Checks shot for a hit, miss, or completed ship and returns
    """
    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                comp.append(shot)
                missed = 2
    if missed == 0:
        miss.append(shot)

    return ships, hit, miss, comp, missed


def get_shot(guesses):
    """
    User input which only allows integer value.
    User feedback of error if not a number.
    Checks if input has already been used in previous turn.
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("Enter a number (0-99) to shoot: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("\nInvalid number, please try again")
            elif shot in guesses:
                print("\nInvalid number, you have shot at this location!")
            else:
                ok = "y"
                break
        except Exception:
            print("\nInvalid entry - Input must be a number 0-99")

    return shot


def check_if_empty(list_of_lists):
    """
    Checks to see if all ships are sunk
    """
    return all([not elem for elem in list_of_lists])


# Before game
hit = []
miss = []
comp = []
guesses = []
missed = 0
taken = []

# Game amount of ships and sizes
battleships = [5, 4, 3, 2, 1]
# Creates a board for player
ships, taken = create_boats(taken, battleships)

# The Loop
for i in range(100):

    # Player shoots
    guesses = hit + miss + comp
    shot = get_shot(guesses)
    ships, hit, miss, comp, missed = check_shot(shot, ships, hit, miss, comp)
    show_board(hit, miss, omp)
# Repeat until ships empty
    if check_if_empty(ships):
        print("You sunk all of the ships in", i + 1, "shots! YOU WIN!")
        break
print("End of game.")
