"""Chapter 05 Practice 2 Program - Passing Values

Assignment Requirements:
Create a program that asks a user to enter a whole number between 20 and 100.
Send that number to a function that will validate the number, and if it is not a number between 20 and 100,
use a while loop to keep asking the user for a valid number. Return the number to the main function.

hint good_number = validate(num) - use a variable to store the returned value

In addition, create three functions that determine if the number is divisible by two, by three,
and by five respectively.

Pass all the results to a final function that displays output on the screen - identifying whether
the number is divisible by two, three, and five."""


def main():
    entered_number = int(input("Please enter a whole number between 20 and 100: "))
    entered_number = validate(entered_number)
    bool_two = divisible_by_two(entered_number)
    bool_three = divisible_by_three(entered_number)
    bool_five = divisible_by_five(entered_number)
    display_results(entered_number, bool_two, bool_three, bool_five)


def validate(number):
    while number < 20 or number > 100:
        print("You entered an invalid number")
        number = int(input("Please enter a whole number between 20 and 100: "))

    return number


def divisible_by_two(number):
    if number % 2 == 0:
        divisible = True
    else:
        divisible = False

    return divisible


def divisible_by_three(number):
    if number % 3 == 0:
        divisible = True
    else:
        divisible = False

    return divisible


def divisible_by_five(number):
    if number % 5 == 0:
        divisible = True
    else:
        divisible = False

    return divisible


def display_results(number, two, three, five):
    if str(two) == "True":
        print(number, "is divisible by two")
    else:
        print(number, "is not divisible by two")

    if str(three) == "True":
        print(number, "is divisible by three")
    else:
        print(number, "is not divisible by three")

    if str(five) == "True":
        print(number, "is divisible by five")
    else:
        print(number, "is not divisible by five")


main()
