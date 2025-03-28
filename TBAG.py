# Cairo Taylor and James Wilcox , Text-Based Adventure Game
import random
def battle(creature, action, location1, location2):
    print(f"The {creature}, positioned in front of you, is ready to strike!")
    print(f"1 is {location1}, 2 is {location2}.")
    move = input(f"Where do you plan to {action}?\n")
    if slingshot == "Yes":
        defense = random.randint(1,2)
    else:
        defense = random.randint(1,5)
    if defense == move:
        print(f"The {creature} predicted your move!")
        print(dedend)
    else:
        print(f"You surprised the {creature} and it fled!")




def split(choice1, choice2):
   print(f"You see 2 pathways that you could take. Do you want to: \n1. {choice1},\nOR\n2. {choice2}?")








befriend = "You managed to befriend the bird! You managed to get the best ending."
sneakend = "You manage to sneak to the surface world and not get eaten. Congratulations! However, that bird could have been friendly! You got the default ending."
dedend = "You failed to escape! You got the worst ending."








firstpick = split("Go down hamster tube slide", "Jump across the glass bridge(1 in 33554432 success)")
frstchoice = int(input("1 or 2:\n"))
if frstchoice == 1:
   print("You decide to go down the hamster tube slide.")
   slingshot = input("At the bottom, you see a tiny slingshot and a bag of tough seeds. Do you pick it up?\n").capitalize()
   if slingshot == "Yes":
       print("You now have a slingshot!")
   else:
       print("You decide to leave it behind.")
   print("Continuing on, you come along another split decision")
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
                   print("You decide to go down the flame lit tunnel. You see a figure by the fire. It is tall and skinny, but you can only see the silouette. It turns its head at you, revealing luminous red eyes.\nIt comes after you!")
                   # Battle Sequence and sneak escape if victory
               else:
                   print("Deciding that the flame is a little suspicious, you decide to crawl into the sewer grate and sneak below the sewer.\nYou close the sewer grate with a slam. A sound of surprise comes from near the fire, followed by a noise like a snake hissing, and then wet footsteps coming in your direction.")
                   fourthchoice = split("Solve the puzzle and continue under the sewer", "Hide quietly and wait for the entity to pass")
                   frthchoice = int(input("1 or 2:\n"))
                   if frthchoice == 1:
                       print("You decide that this entity will be anything but friendly, and that solving the puzzle will be best for you.")
                       puzzle2 = "Yes"
                       while puzzle2 == "Yes":
                        result = input("I am something people either celebrate or resist. I change people’s thoughts and lives. I am obvious to some people but, to others, I am a mystery. What am I?\n").capitalize()
                        if result == "Age":
                            puzzle2 = 0
                            print("The door opens.")
                            break
                        else:
                            print(f"That is incorrect.")
                       print("You hear something lurking behind you...")
                       shadowman = battle("Shadow Man", "swing", "Head", "legs")
                       
                   else:
                       print("You decide that this entity is not intelligent enough to find you in the grate and will pass overhead.\nSuddenly, you see the creature to be a very tall and lanky shadow figure with luminous red eyes. It wraps its arm tentacles around you and you start to choke.")
                       choke = random.randint(1,10)
                       chokblok = int(input("Pick a number between 1 and 10 to see if you can survive this creature's attack."))
                       if chokblok == choke:
                           print("You managed to block the creature's attack, and in the process stun it! Deciding that you may no longer go back through the way you came, you continue on, Eventually finding an escape hatch.")
                           print(sneakend)
                       else:
                           print("The creature's grip strengthens. In one last desperate attempt to escape, you kick it in the leg, but your leg passes though it.")
                           print(dedend)
                     
           else:
               print("No, that is incorrect.")
     
   else:
       print("Because the sewer sounds a little unsafe(or nasty), you decide to keep walking alongside the dungeon. You hear noises coming from each of the cells in the dungeon.")
       scndpick = split("Check out the other dungeon cells", "Walk past them")
       secondchoice = int(input("1 or 2:\n"))
       if secondchoice == 1:
           print("You decide that you want to see what is in the other cells of this dungeon. You walk by the cells and see nothing in them. Confused, you start thinking of something.")
           thrdpick = split("Look closer at the cells", "Ignore them")
           thirdchoice = int(input("1 or 2:\n"))
           if thirdchoice == 1:
               print("A blurry figure seems to materialize. It looks like an old man in chains looking away from you.\n")
               print("You feel a chilly breeze blow through you...")
               ghostman = battle("Prisoner Ghost", "throw a punch", "Head", "Torso")
               
           else:
               print("You decide to continue past them, and run past all the cells. After a few minutes of running, you find yourself exhausted. You also observe that you made it onto a bridge above the lava.")
               print("Something flaps above you...")
           if slingshot == "Yes":
            giantbird = battle("Dragon Bird", "fire a seed", "Head", "Wings")
           else:
            giantbird = battle("Dragon Bird", "throw a seed", "Head", "Wings")
           print("You've scared it off for now, but you have a feeling it'll return.")

       else:
           print("Deciding that it might be dangerous to check out what is in the cells, you run past all the cells.\nAfter a few minutes of running, you find yourself exhausted. You also observe that you made it onto a bridge above the lava.")
           print("Something flaps above you...")
           if slingshot == "Yes":
            giantbird = battle("Dragon Bird", "fire a seed", "Head", "Wings")
           else:
            giantbird = battle("Dragon Bird", "throw a seed", "Head", "Wings")








else:
   print("You decide to go on the glass bridge.")
   count = 0
   while count != 26:
       strong = random.randint(1,2)
       print (strong)
       panes = int(input("You are on the glass bridge. Pick 1 or 2.\n"))
       if panes == strong:
           print("You have made it to the next pane.")
           count += 1
       else:
           print("You have fallen into the lava.")
           print(dedend)
           break
   print(sneakend)


