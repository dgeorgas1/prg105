"""Chapter 06 Assessment Program - Files and Exceptions

Assignment Requirements:
Use Practice 2 Program - Reading Files as a start. Modify the program to do the following:

Request the data file name from the user.
Use a try-except statement to detect errors when opening the file. Report any errors to the screen.
Download the file sales_error-1.txt Download sales_error-1.txt to use as an input file.
Use try-except to detect bad data in the input file. Report it to the screen and skip over bad values.
Total and average the remaining good data and display results."""


def main():  # Define main function
    total = 0  # Initialize total
    number_of_entries = 0  # Initialize number_of_entries

    file_name = input("Enter the name of your data file: ")

    try:  # Try to open file
        file = open(file_name, 'r')  # Open txt file for reading

        for line in file:  # Loop through each line in file
            try:  # Try to convert line to float
                value = float(line.rstrip('\n'))  # Strip new line and convert value to float
                total += value  # Add value to total
                number_of_entries += 1  # Add 1 to number_of_entries
                print(format(value, ',.2f'))  # Print value

            except ValueError:  # Conversion failed
                print("Line", number_of_entries + 1, "wih a value of", line, "is invalid")

        file.close()  # Close txt file

        average = total / number_of_entries  # Divide total by number_of_entries to get average

        print("\nTotal:", format(total, ',.2f'), "\nNumber of Entries:", format(number_of_entries, ',.2f'),
              "\nAverage:", format(average, ',.2f'))  # Print total, number_of_entries and average

    except FileNotFoundError:  # File was not found
        print("Unable to find file", file_name)


main()  # Call main function
