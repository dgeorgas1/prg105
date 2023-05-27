"""Chapter 04 Assessment Program - Repetition Structures

Assignment Requirements:
Write a program that projects yearly income, the amount saved towards retirement each year,
and total retirement savings. Assume a 3 percent raise on the starting income each year,
and a 6% yearly return on investment. You will need to ask the user their current age,
at what age they want to retire, what their current income is,
what percent of their income they save each year, and how much they currently have in savings.
You will calculate how many years until retirement, and display the projected income, savings contribution,
and total savings each year."""

income_raise_percentage = .03
yearly_return_percentage = .06
year = 1

current_age = int(input("What is your current age?: "))
retirement_age = int(input("What is your retirement age?: "))
current_income = int(input("What is your current income?: "))
income_saving_percentage = int(input("What percent of your income do you save per year?: "))
current_savings = int(input("What is your current savings?: "))

"""Calculate years_til_retirement and convert income_saving_percentage to a decimal"""
years_til_retirement = retirement_age - current_age
income_saving_percentage = income_saving_percentage / 100

"""Print column headers"""
print("\nThis projection assumes a 3% raise each year and a 6% yearly return on investment")
print('{:25}'.format("\nYear") + '{:25}'.format("Income") + '{:25}'.format("Saving Contributions") +
      '{:25}'.format("Total Savings"))

"""Calculate year_savings_contribution and total_savings
   Print the year number, current_income, year_savings_contribution and total_savings formatting the column width
   Calculate the income for the next year
   Update the savings
   Add 1 to the year count"""
for age in range(years_til_retirement, 0, -1):
    year_savings_contribution = current_income * income_saving_percentage
    total_savings = current_savings * yearly_return_percentage + year_savings_contribution + current_savings
    print('{:25}'.format(str(year)) + "$" + '{:25}'.format(format(int(current_income), ',')) + "$" +
          '{:25}'.format(format(int(year_savings_contribution), ',')) + "$" +
          '{:25}'.format(format(int(total_savings), ',')))
    current_income += current_income * income_raise_percentage
    current_savings = total_savings
    year += 1
