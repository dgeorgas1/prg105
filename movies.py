"""Chapter 10 Assessment Program - Movies

Assignment Requirements:
Create a class Movie with the following attributes: title, release_year, story_year. Create appropriate setter
and getter methods.

Download the comma separated data file:  MarvelMovies.csvDownload MarvelMovies.csv

Create a program that reads in the comma separated data file and loads the data from each line into a Movie object.
Each line of data contains title, release year, and story year in that order. Store the Movie objects in a list.
Use try-except as appropriate.

Tip-full-size-gold-1.png Hint: Remember to strip off the newline and split the data using commas.

Display the movies in alphabetical order. Format the data into columns with appropriate headings.

Tip-full-size-gold-1.png Hint: Iterate through a sorted list of the movie titles and use a nested loop to display
the details for each movie."""


class Movie:
    # Define initializer method
    def __init__(self, title=0, release_year=0, story_year=0):
        self.__title = title
        self.__release_year = release_year
        self.__story_year = story_year

    # Define less than behavior method
    def __lt__(self, other):
        return self.__title < other.__title

    # Define set_title mutator method
    def set_title(self, title):
        self.__title = title

    # Define set_release_year mutator method
    def set_release_year(self, release_year):
        self.__release_year = release_year

    # Define set_story_year mutator method
    def set_story_year(self, story_year):
        self.__story_year = story_year

    # Define get_title accessor method
    def get_title(self):
        return self.__title

    # Define get_release_year accessor method
    def get_release_year(self):
        return self.__release_year

    # Define get_story_year accessor method
    def get_story_year(self):
        return self.__story_year


def main():  # Define main function
    file = 0  # Initialize file to 0
    movies = []  # Initialize movies list to empty

    try:  # Try to open file
        file = open("MarvelMovies.csv", "r")  # Open file for reading
    except FileNotFoundError:  # If not found
        print("Error - The file was not found")  # Print message Error - The file was not found

    for line in file:  # Loop through each line in file
        line = line.strip('\n').split(",")  # Split the line at comma and strip the new line
        # Assign each part of split line to corresponding variable
        title, release_year, story_year = [i.strip() for i in line]
        movie = Movie()  # Create instance object for Movie class
        movie.set_title(title)  # Set title attribute
        movie.set_release_year(release_year)  # Set release_year attribute
        movie.set_story_year(story_year)  # Set story_year attribute
        movies = movies + [movie]  # Add instance object to movies list

    movies.sort()  # Sort movies list

    print("{: ^35} {: ^15} {: ^15}".format("Title", "Release", "Storyline"))  # Print formatted column headers

    for item in movies:  # Loop through each item in movies list
        title = item.get_title()  # Get title attribute
        release_year = item.get_release_year()  # Get release_year attribute
        story_year = item.get_story_year()  # Get story_year attribute
        print("{: <35} {: ^15} {: ^15}".format(title, release_year, story_year))  # Print formatted data


main()  # Call main function
