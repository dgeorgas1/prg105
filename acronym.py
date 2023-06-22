"""Chapter 08 Practice 1 Program - Acronym

Assignment Requirements:
For this program you will get a phrase from the user, split the phrase into a list, and use the first letter
of each word to create an acronym. Display the acronym using all capital letters."""


def main():  # Define main function
    acronym = ""  # Initialize acronym string to empty

    phrase = input("Please enter a phrase to convert: ")  # Ask for a phrase to convert

    phrase = phrase.split()  # Split phrase into items

    for word in phrase:  # Iterate through each item in phrase
        acronym += word[0].upper()  # Convert the first character in item to uppercase and add to acronym

    print(acronym)  # Print acronym


main()  # Call main function
