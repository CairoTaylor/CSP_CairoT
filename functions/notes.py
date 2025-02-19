#Cairo Taylor, Functions Notes

#Function is action stored by keyword

def add(num1, num2):
    print(num1+num2)

#add(12, 20)
#add(14, 5)
#add(int(input("Tell me a number:\n")), 45)

def user(word):
    answer = input(f"Tell me a {word}:\n")
    return answer

name = user("name").capitalize()
verbing = user("present tense verb").lower()
place = user("place").capitalize()
print(f"{name} was {verbing} to {place}.")