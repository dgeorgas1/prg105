"""Chapter 06 Practice 2 Program - Reading Files

Assignment Requirements:
Write a program that will read numeric data from a text file line by line using a loop.
Strip the newline and convert each value to a float, then display it. Use variables to count and
total the entries. At the end, display the total, count and average of the values."""


def main():  # Define main function
    total = 0  # Initialize total
    number_of_entries = 0  # Initialize number_of_entries

    file = open('sales_totals.txt', 'r')  # Open txt file for reading

    for line in file:  # Loop through each line in file
        value = float(line.rstrip('\n'))  # Strip new line and convert value to float
        total += value  # Add value to total
        number_of_entries += 1  # Add 1 to number_of_entries
        print(format(value, ',.2f'))  # Print value

    file.close()  # Close txt file

    average = total / number_of_entries  # Divide total by number_of_entries to get average

    print("\nTotal:", format(total, ',.2f'), "\nNumber of Entries:", format(number_of_entries, ',.2f'),
          "\nAverage:", format(average, ',.2f'))  # Print total, number_of_entries and average


main()  # Call main function
