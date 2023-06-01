"""Chapter 05 Assessment Program - Functions

Assignment Requirements:
You are going to write a program that finds the area of a shape for the user.

Warning_red-full-size.png Please note, this is not intended to be an example of the
right way to program. It is practice using global variables, passing values into a function,
and returning values from a function.

Create a menu function called from main that will present the user with the following menu.
This program will find the area of a shape for you.
1. Rectangle
2. Triangle
3. Square
4. Circle
5. Quit
Call a validation function from the main function to validate user input, use a while loop
to validate data. Return the validated number to the main function.
Depending on the number selected, ask the user for the appropriate measurements to
calculate the area of the specified shape (see the sample output) (Ask the user in the menu
and pass the values to the called function)
Call the appropriate function, pass the required values to the function
Return the area to the main function and print it on screen from the main function
The menu should re-display until the user selects quit. Use a while loop in the main method
with a flag to accomplish this.
Create a global variable for pi and use it when calculating the area of a circle."""

pi = 3.14


def main():
    option_one = "Rectangle"
    option_two = "Triangle"
    option_three = "Square"
    option_four = "Circle"
    option_five = "Quit"

    # Print menu of options
    print("This program will find the area of a shape for you")
    print("1.", option_one)
    print("2.", option_two)
    print("3.", option_three)
    print("4.", option_four)
    print("5.", option_five)

    selected_option = int(input("Please enter the number of your selection: "))

    # Call validate function to check if between 1 and 5
    selected_option = validate(selected_option)

    # If number is between 1 and 4
    while selected_option != 5:
        if selected_option == 1:
            width = int(input("Enter the rectangle width in cm: "))
            height = int(input("Enter the rectangle height in cm: "))
            area = rectangle(width, height)  # Call rectangle function to calculate the area
            print("The area of the rectangle is", area, "square cm")

        elif selected_option == 2:
            base = int(input("Enter the triangle base in cm: "))
            height = int(input("Enter the triangle height in cm: "))
            area = triangle(base, height)  # Call triangle function to calculate the area
            print("The area of the triangle is", area, "square cm")

        elif selected_option == 3:
            length = int(input("Enter the square length in cm: "))
            area = square(length)  # Call square function to calculate the area
            print("The area of the square is", area, "square cm")

        else:
            radius = int(input("Enter the circle radius in cm: "))
            area = circle(radius)  # Call circle function to calculate the area
            print("The area of the circle is", area, "square cm")

        # Ask for another number until 5 is entered
        selected_option = int(input("Please enter the number of your selection: "))
        selected_option = validate(selected_option)

    print("Ending program")


# Ask for another number until between 1 and 5 is entered
def validate(option):
    while option < 1 or option > 5:
        print("You have entered an invalid option")
        option = int(input("Please enter a number between 1 and 5: "))

    return option


def rectangle(width, height):
    area = width * height  # Calculate the rectangle area
    return area


def triangle(base, height):
    area = .5 * base * height  # Calculate the triangle area
    return area


def square(length):
    area = length**2  # Calculate the square area
    return area


def circle(radius):
    area = pi * radius**2  # Calculate the circle area
    return area


main()
