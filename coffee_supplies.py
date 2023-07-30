"""Chapter 14 Practice 2 Program - Coffee Supplies

Assignment Requirements:
Using the coffee database created in the previous assignment as your data source, generate a report showing coffee
supplies by category similar to the one below. Each category name should appear only once and categories should be in
alphabetical order. (NOTE: Alphabetizing the products in each category is optional.)

Tip-full-size-gold-1.png Hint: Use the ORDER BY option in your SQL SELECT command."""
import sqlite3


def main():  # Define main
    coffee_connection = None  # Initialize coffee_connection to None

    try:
        coffee_connection = sqlite3.connect('coffee.db')  # Crete connection object
        coffee_cursor = coffee_connection.cursor()  # Crete cursor object

        # Get data from Coffee table sorting by Category
        coffee_cursor.execute("""SELECT Category, Product, Supplier FROM Coffee ORDER BY Category""")
        results = coffee_cursor.fetchall()  # Fetch data

        print(f"{'Category':^10} {'Product':^20} {'Supplier':^15}")  # Print column headers
        print('-----------------------------------------------')

        # Initialize category to first category
        category = results[0]
        category = category[0]

        print(category)  # Print the category

        for row in results:  # Loop through each row in results
            if row[0] != category:  # Check if category index does not equal category
                category = row[0]  # If so, update the category
                print(f'{category:10}')  # Print the category

            print(f"{' ':10} {row[1]:20} {row[2]:15}")  # Print the Product and Supplier
    except sqlite3.Error as error:
        print(error)  # Print error message
    finally:
        if coffee_connection is not None:  # Check if database connection was opened
            coffee_connection.close()  # If so, close the connection


main()  # Call main
