# Cairo Taylor, Loops Notes

# What is a loop?
    # A section of code that will repeat 

# What are the two types of loops?
    # While loop
x = 0
while x < 10:
    print("Hello", x)
    x += 1

# For loop
nums = [3,5,7,2,8]
for num in nums:
    print(num)

# What is iteration?
    # The act of repitition

# What are lists?
    # Values in the same variable
siblings = ["Fenix", "Cairo", "Berlin", "Zurich", "Boogly"]

# Print 1 item from the list
print(siblings[1])

# Change an item in a list
siblings[2] = "Stinky"

# Remove item in a list
siblings.pop(4)
num = 1

# Proper list printing
for sibling in siblings:
    print(f"{num}. {sibling} Taylor")
    num +=1



# How do you make lists in python?
    # list_name["item1", "item2", "item3"]

# How do you make for loops in python?
for num in range(2, 11, 2):
    print(num)

# How do you make while loops in python?
num = 1

while num < 21:
    print(f"You are smelly times {num}")
    num += 1

import random

num = 1
rand = random.randint(1,20)
while num <21:
    if num == rand:
        print("GOOSE")
        break
    else:
        print("Duck...")
    num +=1

# Continue tells the loop to stop the particular round of the loop
