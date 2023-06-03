"""Chapter 06 Practice 1 Program - Address Book

Assignment Requirements:
Write a program that gathers contact information from people. The program should ask the user how many entries
they are going to make, then ask for the Name, phone number, and email address for each person.

You will be writing this information to a text file. Separate each value with a comma, and make sure to include
the new line character.

Write this program using a function  - you should just need the main function."""


def main():
    number_of_entries = int(input("How many people do you want to add to the file?: "))

    address_book = open('address_book.txt', 'w')

    for contact in range(1, number_of_entries + 1):
        name = input("What is their name?: ")
        phone_number = input("What is their phone number?: ")
        email_address = input("What is their email address?: ")

        address_book.write(name + ', ' + phone_number + ', ' + email_address + '\n')

    address_book.close()


main()
