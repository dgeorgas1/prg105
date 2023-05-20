"""Chapter 02 Assessment Program Logic - Input, Output

Assignment Requirements:
For this assignment, you will be providing the logic (plan) for the following program:

Create a program that helps someone create a budget. It should ask the user for monthly income
and for each of the following expenses:
Housing
Food
Transportation
Phone
Utilities
Clothing
The program should get input from the user and convert each of the inputs to floats.
The program should calculate and display the income percentage of each budget item.
The program should also tell the user how much money they have left after subtracting
the budgeted items from the income.
Submit you plan as a Word document or plain text file (.txt).
"""

"""Ask the user to enter their monthly income and spending's for each expense type
Convert each expense type that was entered to a float by using float()"""
monthly_income = float(input("How much is your monthly income? "))
housing = float(input("How much do you spend on housing per month? "))
food = float(input("How much do you spend on food per month? "))
transportation = float(input("How much do you spend on transportation per month? "))
phone = float(input("How much do you spend on your phone per month? "))
utilities = float(input("How much do you spend on utilities per month? "))
clothing = float(input("How much do you spend on clothing per month? "))

"""Calculate the percent each expense type is of the monthly income"""
housing_percent = housing / monthly_income
food_percent = food / monthly_income
transportation_percent = transportation / monthly_income
phone_percent = phone / monthly_income
utilities_percent = utilities / monthly_income
clothing_percent = clothing / monthly_income

"""Subtract each expense type from the monthly income to get money left"""
monthly_left = monthly_income - housing - food - transportation - phone - utilities - clothing

"""Display the percents each expense_type uses of the monthly_income and the amount of money left"""
print("\nHousing takes up", format(housing_percent, '.2%'), "of your monthly income")
print("Food takes up", format(food_percent, '.2%'), "of your monthly income")
print("Transportation takes up", format(transportation_percent, '.2%'), "of your monthly income")
print("Phone takes up", format(phone_percent, '.2%'), "of your monthly income")
print("Utilities takes up", format(utilities_percent, '.2%'), "of your monthly income")
print("Clothing takes up", format(clothing_percent, '.2%'), "of your monthly income")

print("\nYou have", "$" + format(monthly_left, ',.2f'), "left of your monthly income")
