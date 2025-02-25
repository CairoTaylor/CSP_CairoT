# Cairo Taylor, Old Enough Project

age = int(input("How old are you, chumster?\n"))

if age < 6:
    print("Sorry, but you aren't even old enough to go to school.")
elif age >= 6 and age < 15:
    print("You are old enough to go to school, however your parents have to take you.")
elif age >= 15 and age < 16:
    print("You are old enough to go to school and get your learners permit, but no driving on your own yet.")
elif age <= 16 and age > 18:
    print("You are old enough to go to school and get your drivers license, but no voting for you yet.")
else:
    print("Congratulations! You can drive and vote, and you're also out of school!")