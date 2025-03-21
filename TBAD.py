import random
def split(choice1, choice2):
    print(f"You have 2 pathways. Do you want to: \n{choice1},\nOR\n{choice2}?")

firstpick = split("1. Go down hampster tube slide", "2. Jump across the glass bridge")
choice = int(input("1 or 2:\n"))
if choice == 1:
    print("You decide to go down the hampster tube slide.")
else:
    print("You decide to go on the glass bridge.")
    count = 0
    while count != 26:
        strong = random.randint(1,2)
        panes = int(input("You are on the glass bridge. Pick 1 or 2."))
        if panes == strong:
            print("You have made it to the next pane.")
        else:
            print("You have fallen into the lava.\nYou lost!")
        