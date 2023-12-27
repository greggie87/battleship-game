#Title
print("\nBATTLESHIP GAME!\n")
#Description
print("It is you against the computer! Guess where to shoot in order to sink the computers ship. First to sink all of the opponents ships is the winner!\n")
#Rules

#Game
def get_shot(guesses):
    """
    User input which only allows integer value. User feedback of error if not a number.
    Checks if input has already been used in previous turn.
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Invalid number, please try again")
            elif shot in guesses:
                print("Invalid number, entry has been previously guessed")
            else:
                ok = "y"
                break
        except:
            print("Invalid entry - Input must be a number 0-99")
    return shot

def show_board(hit, miss, comp):
    """
    Game board area
    """
    print("     0  1  2  3  4  5  6  7  8  9\n")

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

def check_shot(shot, boat1, boat2, hit, miss, comp):
    """
    Checks shot for a hit, miss, or completed ship and returns
    """
    
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    else:
        miss.append(shot)
    
     if shot in boat2:
        boat2.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    else:
        miss.append(shot)
   

    return boat1, boat2, hit, miss, comp

boat1 = [22, 23, 24]
boat2 = [55, 45, 35]

hit = []
miss = []
comp = []

# Loop for guesses
for i in range(10):
    guesses = hit + miss + comp
    shot = get_shot(guesses)
    boat1, boat2, hit, miss, comp = check_shot(shot, boat1, boat2, hit, miss, comp)
    show_board(hit, miss, comp)

    if len(boat1) < 1 and len(boat2) < 1:
        print("You sunk all of the ships! YOU WIN!")
        break
print("End of game")