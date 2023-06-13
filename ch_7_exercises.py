"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""

# TODO 7.2 Lists
print("=" * 10, "Section 7.2 lists", "=" * 10)
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test
days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
items = [0] * 5

# 3) Print the contents of your days list using the for operator
for day in days:
    print(day)

# 4) Print the list item that holds the value Saturday from the days list by using its index
index = 0
for day in days:
    if day == 'Sat':
        print(index)
    index += 1

# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)

# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

# TODO 7.3 List Slicing
print("=" * 10, "Section 7.3 list slicing", "=" * 10)
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days
work_days = days[1:6]
print(work_days)

# TODO 7.4 Finding items in Lists with the in Operator
print("=" * 10, "Section 7.4 using the in operator", "=" * 10)
# Use the in operator to determine whether "Tue" is in the list days
# Based on the result, display "yes, Tue is in the list" or "no, Tue is not in the list"
if "Tue" in days:
    print("yes, Tue is in the list")
else:
    print("no, Tue is not in the list")

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)
# 1) Use append() to append the last three months of the year to the list months.
# NOTE: make sure the months are appended as individual list items
months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])
months.append('Oct')
months.append('Nov')
months.append('Dec')

# 2) Get the index of "May" from the months list and print it on screen
print(months.index('May'))

# 3) Sort list3 from exercise 7.2 and print the results on screen
list3.sort()
for val in list3:
    print(val)

# 4) Reverse the order of list3
list3.reverse()

# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)
for num in list3:
    if num == 5:
        del list3[num]

for val in list3:
    print(val)

# 6) Print the maximum value from list3
print(max(list3))

# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year
months_of_the_year = []
for month in months:
    months_of_the_year.append(month)
print(months_of_the_year)

# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results
total = 0
for val in list3:
    total += val
print(total)

# 2) Get the average of values in list3 and print the results
count = 0
for val in list3:
    count += 1
average = total / count
print(average)

# 3) Open the file states.txt in read mode,
# -- read the contents of the file into the list states_list
# -- print the contents of states_list on screen
file = open('states.txt', 'r')
states_list = file.readlines()
file.close()
for index in range(len(states_list)):
    states_list[index] = states_list[index].rstrip('\n')
print(states_list)

# TODO 7.8 List Comprehensions
print("=" * 10, "Section 7.8 list comprehensions", "=" * 10)
# Use list comprehension to create a new list whose values are the squares of my_list's values
# display the new list
my_list = [1, 5, 7, 22, 37, 90]
square_list = [val**2 for val in my_list]
print(square_list)

# TODO 7.9 Two-Dimensional Lists
print("=" * 10, "Section 7.9 two-dimensional lists", "=" * 10)
# 1) Create a new two-dimensional list named days_in_month
#     the outer list should have twelve elements, one for each month
#     the element for each month should be a list holding the month name and number of days
#     So, days_in_month[0][0] is January and days_in_month[0][1] is 31
days_in_month = [["Jan", 31], ["Feb", 28], ["Mar", 31], ["Apr", 30], ["May", 31], ["Jun", 30],
                 ["Jul", 31], ["Aug", 31], ["Sep", 30], ["Oct", 31], ["Nov", 30], ["Dec", 31]]

# 2) Print the contents of the entire list
for month in days_in_month:
    for day in month:
        print(day)

# 3) Print just the values for index 3,0 and 3,1
month_count = 0
for month in months_of_the_year:
    if month_count == 3:
        print(days_in_month[month_count])
    month_count += 1

# TODO 7.10 Tuples
print("=" * 10, "Section 7.10 tuples", "=" * 10)
# Create a tuple using the months list as its data source
create_tuple = tuple(months)