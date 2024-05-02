"""Chapter 12 Assessment Program - CRUD Name and Address Program

Assignment Requirements:
For this assignment you will write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user choose to look up a person's email address, add a new name and
email address, change an existing email address, or delete an existing name and email address. The program should
pickle the dictionary and save it to a file whenever changes are made. Each time the program starts, it should
retrieve the dictionary from the file and unpickle it. The main menu will repeat until the user chooses to QUIT."""

import pickle

# Initialize Global Variables
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():  # Define main function
    try:
        pickled_file = open('pickled_file.dat', 'rb')  # Try to open the pickled_file
        customer_file = pickle.load(pickled_file)  # Unpickle the customer_file
        pickled_file.close()  # Close pickled_file
    except FileNotFoundError:
        customer_file = {}  # Initialize customer_file as an empty dictionary

    choice = 0  # Initialize choice to zero

    while choice != QUIT:
        choice = menu()  # Call menu function

        if choice == LOOK_UP:
            read(customer_file)  # Call read function
        elif choice == ADD:
            create(customer_file)  # Call create function
        elif choice == CHANGE:
            update(customer_file)  # Call update function
        elif choice == DELETE:
            delete(customer_file)  # Call delete function
        else:
            print("Quitting Program")


def menu():  # Define menu function
    choice = 0  # Initialize choice to zero

    while choice not in range(1, 6):  # While choice is not valid
        # Display menu
        print(f'\nEnter your selection:\n{LOOK_UP}. Look up an email by name\n{ADD}. Add a new entry'
              f'\n{CHANGE}. Change a person\'s email\n{DELETE}. Delete an entry\n{QUIT}. Quit\n')
        try:
            choice = int(input("Please select an option: "))  # Ask for user choice and try to convert to int
        except ValueError:  # If failed to convert choice to int
            print("Please enter a number")
    return choice


def read(customer_file):  # Define read function
    customer_name = input("Enter a name: ")

    if customer_name in customer_file:  # Check if customer_name is in customer_file
        print(customer_file[customer_name])  # If so, print email address
    else:
        print("No data found. Try adding a new entry.")


def create(customer_file):  # Define create function
    customer_name = input("Enter a name: ")

    if customer_name not in customer_file:  # Check if customer_name is not in customer_file
        # If true, ask for email and add to customer_file
        customer_email = input("Enter an email address for " + customer_name + ": ")
        customer_file[customer_name] = customer_email
        save(customer_file)  # Call save function
        print(f'{customer_name} has been added with email {customer_email}')
    else:
        print("Unable to add data. The entered name already exists.")


def update(customer_file):  # Define update function
    customer_name = input("Enter a name: ")

    if customer_name in customer_file:  # Check if customer_name is in customer_file
        # If so, ask to confirm change
        answer = input(f'Current email for {customer_name} is {customer_file[customer_name]}. '
                       'Do you want to change it? (y/n): ')
        if answer == 'y':
            # Ask for customer_email and assign to customer_name key for value
            customer_email = input(f'Enter the new email address for {customer_name}: ')
            customer_file[customer_name] = customer_email
            save(customer_file)  # Call save function
            print(f'The email for {customer_name} is now {customer_file[customer_name]}')
        else:
            print("No changes were made.")
    else:
        print("No data found. Try adding a new entry.")


def delete(customer_file):  # Define delete function
    customer_name = input("Enter a name: ")

    if customer_name in customer_file:  # Check if customer_name is in customer_file
        # If so, ask to confirm deletion
        answer = input(f'Current email for {customer_name} is {customer_file[customer_name]}. '
                       'Are you sure you want to delete it? (y/n): ')
        if answer == 'y':
            del customer_file[customer_name]  # Delete customer_name from customer_file
            save(customer_file)  # Call save function
            print(f'{customer_name} has been removed.')
        else:
            print("No changes were made.")
    else:
        print("No data found. Try adding a new entry.")


def save(customer_file):  # Define save function
    try:
        pickled_file = open('pickled_file.dat', 'wb')  # Try to open the pickled_file
        pickle.dump(customer_file, pickled_file)  # Pickle the customer_file
        pickled_file.close()  # Close pickled_file
    except FileNotFoundError:
        print("Warning - Unable to save file.\n")


main()  # Call main function
