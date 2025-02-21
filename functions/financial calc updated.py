# Cairo Taylor, Financial Calculator Updated

income = float(input("What is your monthly income?\n"))
rent = float(input("What is your monthly rent?\n"))
utilities = float(input("What is your monthly cost of utilities?\n"))
groceries = float(input("What is your monthly cost of groceries?\n"))
transportation = float(input("What is your monthly cost of transportation?\n"))
savings = float(income / 10)
spending = float(income - rent - utilities - groceries - transportation)
perspending = float((spending / income) * 100)

def info(income, amount, type):
    pertype = amount/income*100
    print(f"You spend ${amount:.2f} on {type}, which is {pertype:.0f}% of your monthly income")
    return amount

info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")
print(f"The amount of money you have saved for future use is", round(savings, 0), "which is 10% of your income")
print("The money you have left for spending is", round(spending, 0), "which is", round(perspending, 0), " percent of your income")