#Cairo Taylor, Hello World Updated



def title(count):
    answor = input(f"Tell me person #{count}'s name:\n")
    return answor

first = title("1").capitalize()
print(f"Hello, {first}! It's nice to meet you!")

second = title("2").capitalize()
print(f"Hello, {second}! It's nice to meet both you and {first}!")

third = title("3").capitalize()
print(f"Hello, {third}! It's nice to meet you, {second}, and {first}!")

fourth = title("4").capitalize()
print(f"Hello, {fourth}! It's nice to meet you, {third}, {second}, and {first}!")

fifth = title("5").capitalize()
print(f"Hello, {fifth}! It's nice to meet you, {fourth},  {third}, {second}, and {first}!")
# Hello, Sadfjaaaaaaaa!
# Best name there was