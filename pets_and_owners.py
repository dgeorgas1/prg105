"""Chapter 14 Assessment Program - Pets and Owners

Assignment Requirements:
For this assignment, you will be providing the logic (plan) for the following program:

For this assignment you will create a database that holds two related tables: Owners and Pets. You will read in
comma-delimited text files to insert data into each of the tables. Finally, you will display the data in a report
grouped by owner.

1. Download both comma-delimited data files:

Owners.txt

Pets.txt

2. Create an SQLite database named pets.db and add the related tables Owners and Pets. The Pets table should include a
field that links to the OwnerID field.  Use the following SQL statements to create the tables with a one-to-many
relationship:

Owners:

CREATE TABLE IF NOT EXISTS Owners (OwnerID INTEGER PRIMARY KEY NOT NULL, OwnerName TEXT, OwnerPhone TEXT)

Pets:

CREATE TABLE IF NOT EXISTS Pets (PetID INTEGER PRIMARY KEY NOT NULL, PetName TEXT, PetType TEXT, PetBreed TEXT,
OwnerID INTEGER, FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID))

Hint: You can copy/paste this code into your execute statement(s) to ensure correct SQL syntax.

3. Read in the comma-delimited text files and insert the data into their respective tables.

Hint: Remember to commit your changes to the database.

4. Using nested loops, display the pet information below each owner as shown in the sample output."""
import sqlite3


def main():  # Define main
    pets_connection = None  # Initialize connection to None

    try:
        pets_connection = sqlite3.connect('pets.db')  # Create connection object
        pets_cursor = pets_connection.cursor()  # Create cursor object

        # Create Owners table
        pets_cursor.execute("""CREATE TABLE IF NOT EXISTS Owners (OwnerID INTEGER PRIMARY KEY NOT NULL, OwnerName TEXT,
                               OwnerPhone TEXT)""")
        pets_connection.commit()  # Save changes to pets.db database

        # Create Pets table
        pets_cursor.execute("""CREATE TABLE IF NOT EXISTS Pets (PetID INTEGER PRIMARY KEY NOT NULL, PetName TEXT,
                               PetType TEXT, PetBreed TEXT, OwnerID INTEGER,
                               FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID))""")
        pets_connection.commit()  # Save changes to pets.db database

        try:
            file = open('Owners.txt', 'r')  # Try to open file for reading

            for line in file:  # Loop through each line in file
                line = line.strip('\n').split(',')  # Split line at commas stripping the new line

                # Insert data into Owners table
                pets_cursor.execute("""INSERT INTO Owners (OwnerName, OwnerPhone) VALUES (?, ?)""", (line[0], line[1]))
                pets_connection.commit()  # Save changes to pets.db database

            file.close()  # Close the file
        except FileNotFoundError:
            print("File was not found.")  # Print message File was not found

        try:
            file = open('Pets.txt', 'r')  # Try to open file for reading

            for line in file:  # Loop through each line in file
                line = line.strip('\n').split(',')  # Split line at commas stripping the new line

                # Insert data into Pets table
                pets_cursor.execute("""INSERT INTO Pets (PetName, PetType, PetBreed, OwnerID) VALUES (?, ?, ?, ?)""",
                                    (line[0], line[1], line[2], line[3]))
                pets_connection.commit()  # Save changes to pets.db database

            file.close()  # Close the file
        except FileNotFoundError:
            print("File was not found.")  # Print message File was not found

        # Get data
        pets_cursor.execute("""SELECT OwnerName, OwnerPhone, PetName, PetType, PetBreed FROM Owners, Pets
                               WHERE Owners.OwnerID == Pets.OwnerID""")
        results = pets_cursor.fetchall()  # Fetch data

        first_line = results[0]  # Get the first line
        name = first_line[0]  # Get name
        phone = first_line[1]  # Get phone number

        print(f'{name:16} {phone:12}')  # Print name and phone number

        for row in results:  # Loop through each row in results
            if row[0] != name:  # Check if name index does not equal name
                name = row[0]  # If so, update the name
                print(f'{name:16} {row[1]:12}')  # Print the name and phone number

            print(f"{' ':6} {row[2]} is a {row[4]} {row[3]}.")  # Print the pet name, type and breed
    except sqlite3.Error as error:
        print(error)  # Print error message
    finally:
        if pets_connection is not None:  # Check if database connection was opened
            pets_connection.close()  # If so, close the connection


main()  # Call main
