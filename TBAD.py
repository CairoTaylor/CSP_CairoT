# Cairo Taylor and James Wilcox , Text-Based Adventure Game
import random

def sneakend():
    print("You manage to sneak to the surface world and not get eaten. Congratulations! However, that bird could have been friendly!")
    
def split(choice1, choice2):
    print(f"You see 2 pathways that you could take. Do you want to: \n1. {choice1},\nOR\n2. {choice2}?")

print("You wake in a giant bird cage. You don't want to fall into the lake of lava below or get eaten by the big bird flying around.")

firstpick = split("Go down hampster tube slide", "Jump across the glass bridge(1 in 33554432 success)")
frstchoice = int(input("1 or 2:\n"))
if frstchoice == 1:
    print("You decide to go down the hampster tube slide.")
    slingshot = input("At the bottom, you see a tiny slingshot. Do you pick it up?\n").capitalize()
    if slingshot == "Yes":
        print("You now have a slingshot!")
    else:
        print("You decide to leave it behind.")
    print("Continuing on, you come along another split desicion")
    secondpick = split("Unlock sewer gate", "Walk along the side of the dungeon")
    scndchoice = int(input("1 or 2:\n"))
    if scndchoice == 1:
        print("You decide to go through the sewer gate, after you complete the riddle to unlock it first.")
        puzzle1 = ("Yes")
        print("Time flies like an arrow, and fruit flies like a...")
        while puzzle1 == "Yes": 
            solution = input("What is the answer?: ").capitalize()
            if solution == "Banana":
                puzzle1 = ("No")
                print("Congratulations! You did it! You can now enter into the sewer. Look out for Ninja Turtles! If you have any pizza on you, it would be a good idea to discard it.")
                thirdpick = split("Go down the flame-lit tunnel", "Crawl through the grate system")
                thrdchoice = int(input("1 or 2:\n"))
                if thrdchoice == 1:
                    print("You decide to go down the flame lit tunnel. You see a figure by the fire. It is tall and skinny, but you can only see the silouette. It turns its head at you, revealing luminous red eyes.")
                    # Battle Sequence and sneak escape if victory
                else:
                    print("Deciding that the flame is a little suspicious, you decide to crawl into the sewer grate and sneak below")
            else:
                print("No, that is incorrect.")
        
    else:
        print("Because the sewer sounds a little unsafe(or nasty), you decide to keep walking alongside the dungeon.")

else:
    print("You decide to go on the glass bridge.")
    count = 0
    while count != 26:
        strong = random.randint(1,2)
        panes = int(input("You are on the glass bridge. Pick 1 or 2.\n"))
        if panes == strong:
            print("You have made it to the next pane.")
            count += 1
        else:
            print("You have fallen into the lava.\nYou lost!")
            break