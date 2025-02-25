# Cairo Taylor, Conditionals Notes

print("Hello and welcome to my program that will sort you into a category.")

name = input("What is your name?\n").strip().capitalize()

if name == "Terhg":
    print("You have the best name in the entire universe.")
elif name == "Cairo":
    print("All hail the creator...")
else:
    print("You fall under the category of: stupid.")

num = int(input("How many would you like? (number you idiot)\n"))

if num == 1:
    print("You have asked for an item.")
elif num <= 3:
    print("You have asked for a couple of the item.")
elif num <= 5:
    print("You have asked for a few of the item.")
else:
    print("You have asked for some of the item.")


if "a" in name:
    print("Your name has the letter a.")
else:
    print("Your name doesn't have an a in it.")

if name == "Terhg":
    print("You have the best name in any universe")
elif "a" in name or "e" in name or "i" in name or "o" in name or "u" in name:
    print("CONGRATULATIONS! YOUR NAME IS REGULAR AND HAS A VOWEL!")
else:
    print("Wtf is wrong with your name it has no vowels.")

if "J" and "I" in name:
    print("You have a J and an I in your name, which is pretty crazy ngl.")
else:
    print("You don't got a J and an I in your name.")