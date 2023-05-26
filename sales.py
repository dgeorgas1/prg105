"""Chapter 04 Practice 1 Logic - Sales

Assignment Requirements:
For this assignment, you will be providing the logic (plan) for the following program:

Create a program that will have the user enter the total sales amount for the day at a coffee shop.
The program should ask the user for the total amount of sales and include the day in the request.
At the end of data entry, tell the user the total sales for the week, and the average sales per day.
You must create a list of the days of the week for the user to step through, see the example output."""

total_sales = 0
number_of_days = 0

for day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
    total_sales += float(input("What were the total sales for " + day + "?: "))
    number_of_days += 1

average_sales = total_sales / number_of_days

print("\nThe total amount of sales for the week was:", "$" + format(total_sales, ',.2f'))
print("The average amount of sales per day was:", "$" + format(average_sales, ',.2f'))
