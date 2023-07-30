"""Chapter 14 Practice 1 Logic - Make Coffee

Assignment Requirements:
For this assignment, you will be providing the logic (plan) for the following program:

Create an SQLite database with one table named Coffee. The table should have the following fields:

ProductID INTEGER PRIMARY KEY NOT NULL
Product TEXT
Category TEXT
Supplier TEXT
Insert data into the Coffee table using the data provided in the comma-delimited text file: coffeehouse_supplies.csv

Tip-full-size-gold-1.png Hint: The data is comma-separated - split on commas.

Tip-full-size-gold-1.png Hint: Refer to Inserting the Values of Variables in section 14.5 of your book for an example
of using INSERT with variable values.

Display the number of records successfully added, or an appropriate error message."""
import sqlite3


def main():  # Define main
    coffee_connection = None  # Initialize coffee_connection to None

    try:
        coffee_connection = sqlite3.connect('coffee.db')  # Crete connection object
        coffee_cursor = coffee_connection.cursor()  # Crete cursor object

        coffee_cursor.execute("""CREATE TABLE Coffee (ProductID INTEGER PRIMARY KEY NOT NULL, Product TEXT, 
                                 Category TEXT, Supplier TEXT)""")  # Create Coffee table
        coffee_connection.commit()  # Save changes to coffee.db database

        try:
            file = open('coffeehouse_supplies.csv', 'r')  # Try to open file for reading

            for line in file:  # Loop through each line in file
                line = line.strip('\n').split(',')  # Split line at commas stripping the new line

                # Insert data into Coffee table
                coffee_cursor.execute("""INSERT INTO Coffee (Product, Category, Supplier) 
                                         VALUES (?, ?, ?)""", (line[0], line[1], line[2]))
                coffee_connection.commit()  # Save changes to coffee.db database

            coffee_cursor.execute("""SELECT * From Coffee""")  # Get all data from Coffee table
            results = coffee_cursor.fetchall()  # Fetch data

            print(f"{'ID':^2} {'Product':^20} {'Category':^10} {'Supplier':^15}")  # Print column headers
            print('--------------------------------------------------')
            for row in results:  # Loop through fetched data
                print(f'{row[0]:<2} {row[1]:<20} {row[2]:<10} {row[3]:<15}')  # Print formatted data

            coffee_cursor.execute("""SELECT COUNT(*) FROM Coffee""")  # Get count from Coffee table
            row_count = coffee_cursor.fetchone()  # Fetch data
            print(f'\n{row_count[0]} records were added.')  # Print number of records added

        except FileNotFoundError:
            print("File was not found.")  # Print message File was not found
    except sqlite3.Error as error:
        print(error)  # Print error message

    except IOError:
        print("Unable to add data.")  # Print message Unable to add data

    finally:
        if coffee_connection is not None:  # Check if database connection was opened
            coffee_connection.close()  # If so, close the connection


main()  # Call main
