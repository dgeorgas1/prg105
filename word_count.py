"""Chapter 09 Assessment Program - Word Count

Assignment Requirements:
Download the following text file:

tale_of_two_cities.txtDownload tale_of_two_cities.txt

Create a program to read the words in the file and add them to a dictionary along with a count of how
many times each word appears in the file. When all words in the file have been added, display the unique
words in the dictionary (i.e. words with a count of 1)."""


def main():  # Define main function
    word = {}  # Initialize word dictionary to empty

    file = open('tale_of_two_cities.txt', 'r')  # Open tale_of_two_cities.txt for reading and assign to file

    for line in file:  # Read each line in file
        if line in word:  # Check if line is found in dictionary
            word[line] += 1  # If so, add 1 to value for key
        else:  # If not found
            word[line] = 1  # Add line to dictionary using word as key and 1 for value

    file.close()  # Close file

    for k in word:  # Loop through word dictionary
        if word[k] == 1:  # Check if value of key is equal to 1
            print(k.rstrip('\n'))  # Print key stripping the new line


main()  # Call main function
