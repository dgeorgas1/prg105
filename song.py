"""Chapter 04 Practice 2 Logic - Song

Assignment Requirements:
Use loops to make all the lyrics of "99 bottles of beer on the wall"  print on the screen.
Adjust the last two verses for correct grammar."""

number_of_bottles = 99

line1 = "bottles of beer on the wall,"
line2 = "bottles of beer"
line3 = "Take one down, pass it around"
line4 = "bottles of beer on the wall\n"

alt_line1 = "bottle of beer on the wall,"
alt_line2 = "bottle of beer"
alt_line4 = "bottle of beer on the wall\n"

while number_of_bottles != 0:
    if number_of_bottles == 2:
        print(number_of_bottles, line1)
        print(number_of_bottles, line2)
        print(line3)
        print(number_of_bottles - 1, alt_line4)

    elif number_of_bottles == 1:
        print(number_of_bottles, alt_line1)
        print(number_of_bottles, alt_line2)
        print(line3)
        print(number_of_bottles - 1, line4)

    else:
        print(number_of_bottles, line1)
        print(number_of_bottles, line2)
        print(line3)
        print(number_of_bottles - 1, line4)

    number_of_bottles -= 1
