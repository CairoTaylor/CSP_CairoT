# Cairo Taylor, Financial Calculator

# Going top to bottom, the averages for all these things I found is 4897, 1828, 345, 606, and 1098
# Write a print statement telling the user what the program is
print("Hello! This is a program for calculating your monthly finances.")
# Ask the user for monthly income
income = float(input("What is your monthly income?\n"))
# Ask for each expense (rent, utilities, groceries, transportation)
rent = float(input("What is your monthly rent?\n"))
utilities = float(input("What is your monthly cost of utilities?\n"))
groceries = float(input("What is your monthly cost of groceries?\n"))
transportation = float(input("What is your monthly cost of transportation?\n"))
# Calculate savings as 10% of income
savings = float(income / 10)
# Calculate spending money: income - rent, utilities, groceries, transportation, and savings
spending = float(income - rent - utilities - groceries - transportation)
# Calculate % of rent (rent/income)*100
perent = float(income / rent * 100)
# Calculate % of utilities (rent/utilities)*100
perutilities = float(income / utilities * 100)
# Calculate % of groceries (rent/groceries)*100
pergroceries = float(income / groceries * 100)
# Calculate % of transportation (rent/transportation)*100
pertransportation = float(income / transportation * 100)
# Tell the user category spending amount and percent for all categories
print("The percent of money from your income used for rent is", round(perent, 2))
print("The percent of money from your income used for utilities is", round(perutilities, 2))
print("The percent of money from your income used for groceries is", round(pergroceries, 2))
print("The percent of money from your income used for transportation is", round(pertransportation, 2))
# Tell the user how much spending money is available
print("The money you have left for spending is", round(spending, 2))
# Tell the user how much money is for saving
print("The amount of money you have saved for future use is", round(savings, 2))