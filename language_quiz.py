"""Chapter 09 Practice 2 Program - Language Quiz

Assignment Requirements:
Create a dictionary based on the language of your choice with the numbers from 1-10 paired with the numbers
from 1-10 in English. Create a quiz based on this dictionary. Display the number in a foreign language and
ask for the number in English. Score the test and give the user a letter grade.

Tip-full-size-gold-1.png Hint: For this game, ignore accent marks for non-English languages."""


def main():  # Define main function
    # Create language dictionary
    language = {'ein': 'one', 'zwei': 'two', 'drei': 'three', 'vier': 'four', 'funf': 'five', 'sechs': 'six',
                'sieben': 'seven', 'acht': 'eight', 'neun': 'nine', 'zehn': 'ten'}
    number_corrct = 0  # Initialize number_correct to 0

    # Print message describing program
    print("Enter the number in English which corresponds to the number in German.")

    for k in language:  # Loop through each k in language dictionary
        answer = input("What is the equivalent of " + k + "?: ")  # Ask user to enter answer

        while not answer.isalpha():  # Loop if answer is not alpha
            # Ask user to spell out answer
            answer = input("What is the equivalent of " + k + "? (Please spell out the number): ")

        if answer.lower() == language[k]:  # Check if answer is equal to value of key ignoring the case
            number_corrct += 1  # Add 1 to number_correct
            print("Correct")  # Print message Correct
        else:  # If answer is not equal
            # Print message Incorrect. The correct answer is followed by the value of key
            print("Incorrect. The correct answer is " + language[k])

    # Print message Your final score is number_correct / the length of language dictionary
    print("Your final score is", number_corrct, "/", len(language))

    if number_corrct == 9 or number_corrct == 10:  # Check if number_correct is equal to 9 or 10
        print("Grade: A")  # If so, print message Grade: A
    elif number_corrct == 8:  # Check if number_correct is equal to 8
        print("Grade: B")  # If so, print message Grade: B
    elif number_corrct == 7:  # Check if number_correct is equal to 7
        print("Grade: C")  # If so, print message Grade: C
    elif number_corrct == 6:  # Check if number_correct is equal to 6
        print("Grade: D")  # If so, print message Grade: D
    else:  # If number_correct is less than 6
        print("Grade: F")  # Print message Grade: F


main()  # Call main function
