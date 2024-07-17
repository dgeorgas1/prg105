"""Chapter 08 Assessment Program - Strings

Assignment Requirements:
For this assignment, you will compare the contents of two files and display customer information only for
those customers whose accounts are overdue.

Download both files:
accounts.txt Download accounts.txt   # customer accounts

over90.txt Download over90.txt   # overdue account numbers

Read the files into two separate lists. Print the complete customer information on the screen if the customer
number is found in the overdue accounts list. Do error checking for file names to make sure the files
exist (try and except statements.)"""


def main():  # Define main function
    accounts = []  # Initialize accounts list to empty
    overdue_accounts = []  # Initialize overdue_accounts list to empty

    try:  # Try to open files
        with open("accounts.txt", "r") as accounts_file:
            with open("over90.txt", "r") as overdue_accounts_file:

                for line in accounts_file:  # Iterate through each line of account_file
                    accounts.append(line)  # Append line to accounts list

                for line in overdue_accounts_file:  # Iterate through each line of overdue_account_file
                    overdue_accounts.append(line)  # Append line to overdue_accounts list

        for value in overdue_accounts:  # Iterate through each value of overdue_accounts list
            value = value.rstrip('\n')  # Strip the new line
            for line in accounts:  # Iterate through each line in accounts list
                line = line.split(',')  # Split the line at the comma
                if value == line[0]:  # Check if value is equal to position 0 of line
                    print(*line, sep=",")  # If so, print the line separating each position by a comma

    except FileNotFoundError:  # If File Not Found
        print("The file was not found")  # Print message the file was not found


main()  # Call main function
