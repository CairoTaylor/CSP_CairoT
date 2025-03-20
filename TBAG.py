progress = 0
import random
while progress > 25:
    strong = random.randint(1,2)
    choiec = input("Do you choose left(1) or right(2)?\n")
    if choiec == strong:
        print("Congratulations, you can continue.")
        progress += 1
    else:
        print("Oh no! You fall off the bridge and into the lava.")
        if progress != 1:
            print(f"You made it across {progress} panels.")
        else:
            print("You only made it across 1 panel.")
        break