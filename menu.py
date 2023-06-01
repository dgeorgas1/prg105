"""Chapter 05 Practice 1 Program - Menu

Assignment Requirements:
Create a program that presents the user with five choices. The topic could be game characters,
food, car packages, anything you are interested in. You will put a menu on the screen,
ask the user to enter the number or letter of their choice, and then call the corresponding function
to give the user more information."""

option_one = "Cheeseburger"
option_two = "Chicken Parm"
option_three = "Buffalo Chicken"
option_four = "Ruben"
option_five = "Italian Beef"


def main():
    print("Select one of the menu options below to find out more information:")
    print("1.", option_one)
    print("2.", option_two)
    print("3.", option_three)
    print("4.", option_four)
    print("5.", option_five)

    selected_option = int(input("Please enter the number of your choice: "))

    while selected_option < 1 or selected_option > 5:
        print("You did not enter a valid number")
        selected_option = int(input("Please enter a number between 1 and 5: "))

    if selected_option == 1:
        one()
    elif selected_option == 2:
        two()
    elif selected_option == 3:
        three()
    elif selected_option == 4:
        four()
    else:
        five()


def one():
    print("Cheeseburger")
    print("Served with a side of french fries and cole slaw")


def two():
    print("Chicken Parm")
    print("Served with a side of spaghetti and marina sauce")


def three():
    print("Buffalo Chicken")
    print("Served with a side of dressing and tator tots")


def four():
    print("Ruben")
    print("Served with a side of chips and fruit")


def five():
    print("Italian Beef")
    print("Served with a side of giardiniera and french fries")


main()
