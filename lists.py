"""Chapter 07 Assessment Program - Lists

Assignment Requirements:
For this assignment, you will decode the coded message file you created in the Parallel Arrays program:

Create your new program in the same folder used for the Parallel Arrays program. This will give you access to the
file you created in your Parallel Arrays program.
Copy the parallel arrays you used in the original program into your new program -- you will need to use the same
parallel arrays in order to decode the message.
Ask the user for the name of the file to import (the file you created in your previous assignment)
Use try and except statements to ensure the file is there (Use a variable to store the file name, don't hard code it.)
Use read lines to read the file into a list
Step through the list (strip the \n!)
Convert the coded message back into English and display the message on the screen (This can be concatenated to a
string as you decode)
idea-1.png Important! You will be using the same parallel arrays and your output file for your assessment program."""


def main():  # Define main function
    message = ''  # Initialize message to empty

    # Create alpha list
    alpha = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k',
             'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U',
             'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', ' ', '.', ',', '!']

    # Create code list
    code = [' ', 'n', 'N', 'p', 'P', 'r', 'R', 't', 'T', 'a', 'A', 'c', 'C', 'e', 'E', 'g', 'G', 'u', 'U', 'w', 'W',
            'y', 'Y', 'h', 'H', 'j', 'J', '.', ',', 'l', 'L', 'o', 'O', 'q', 'Q', 's', 'S', 'b', 'B', 'd', 'D', 'f',
            'F', 'v', 'V', 'x', 'X', 'z', 'Z', 'i', 'I', 'k', 'K', 'm', 'M', '!']

    file_name = input("What is the name of the file to decode? ")  # Get file_name from input

    try:
        file = open(file_name, 'r')  # Try to open file_name
        coded_message = file.readlines()  # Read lines of file

        for char in coded_message:  # Iterate through coded_message
            message += alpha[code.index(char.rstrip('\n'))]  # Get the char in alpha list from index in code list

        file.close()  # Close the file
        print(message)  # Print message

    except FileNotFoundError:  # Catch exception
        print("File was not found")  # Print error message


main()  # Call main function
