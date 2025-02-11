# Cairo Taylor, Strings Notes

# A string is words in programming (data type) "" ''

print("I'm Mr. King Dice")
print('Im Mr. King Dice') # Use quotation marks when you need apostrophes

name = input("What is your first name?\n").strip().capitalize() # Make sure to add () at the end
print (f"You have a bad name, {name}.")

num = input("Give me a number.\n")

challenge = input("Do you wish to challenge me?\n")
print(challenge.find("yes"))

oogles = "I'm Mr. King Dice, I'm the gamest in the land."
chunk = oogles.find("King Dice")
print(oogles[chunk:chunk+9])
print(f"Are you {name}? I think {name} is very cool.")