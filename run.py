#Title
print("\nBATTLESHIP GAME!\n")
#Description
print("It is you against the computer! Guess where to shoot in order to sink the computers ship. First to sink all of the opponents ships is the winner!\n")
#Rules

#Game
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

hit = [22, 23, 24]
miss = [11,12,13,14]
comp = [25]