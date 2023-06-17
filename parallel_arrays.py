"""Chapter 07 Practice 2 Program - Parallel Arrays

Assignment Requirements:
For this program, you will use parallel arrays (lists) to make a secret code creator. The first array (alpha array)
will hold all upper and lower case letters, space, period, comma, and exclamation point. You will create a second
array of the same size (code array) to hold your secret code characters. Make sure you do not duplicate any
characters. In other words, the letter 'm' might appear in both arrays, but no more than once in each array.

Example:

alpha = ['a', 'A', 'b', 'B' . . . ]   # partial array for the first array

code = ['%', 'm', '#', '='  . . .]   # partial array for corresponding coded characters

With this example, lower-case 'a' would be encoded as '%' since both are found at subscript position zero.

You will ask the user for a secret phrase and encode each character by finding it in the alpha array and displaying
the corresponding character from the code array. You will display the encoded message on-screen as a list and also
write it to a file, one character per line.

idea-1.png Important! You will be using the same parallel arrays and your output file for your assessment program."""


def main():  # Define main function
    phrase = input("Enter a phrase to encode: ")  # Get phrase from user
    find_chars_in_code(phrase)  # Call find_chars_in_code function passing phrase


def find_chars_in_code(phrase):  # Define find_chars_in_code function
    code_chars = []  # Initialize code_chars list to empty

    # Create alpha list
    alpha = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k',
             'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U',
             'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', ' ', '.', ',', '!']

    # Create code list
    code = [' ', 'n', 'N', 'p', 'P', 'r', 'R', 't', 'T', 'a', 'A', 'c', 'C', 'e', 'E', 'g', 'G', 'u', 'U', 'w', 'W',
            'y', 'Y', 'h', 'H', 'j', 'J', '.', ',', 'l', 'L', 'o', 'O', 'q', 'Q', 's', 'S', 'b', 'B', 'd', 'D', 'f',
            'F', 'v', 'V', 'x', 'X', 'z', 'Z', 'i', 'I', 'k', 'K', 'm', 'M', '!']

    file = open('code_a_phrase.txt', 'w')  # Open code_a_phrase.txt for writing

    for char in phrase:  # Iterate through each char in phrase
        line = code[alpha.index(char)]  # Assign the code_char to line
        code_chars.append(line)  # Append line to code_chars list
        file.write(line + '\n')  # Write line to code_a_phrase.txt and add new line

    print(code_chars)  # Print code_chars list

    file.close()  # Close code_a_phrase.txt


main()  # Call main function
