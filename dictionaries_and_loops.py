"""Chapter 09 Practice 1 Program - Dictionaries and Loops

Assignment Requirements:
You will be tracking the number of steps someone takes each day for a week. Using a loop, ask them to enter
the date and the number of steps. At the end of the program, you will display the total number of steps taken,
the day with the most steps, and the day with the least steps. Print multiple days if they are tied.

Tip-full-size-gold-1.png Hint: Use separate loops to display the days for the minimum and maximum values."""


def main():  # Define main function
    steps = {}  # Initialize steps dictionary to empty

    total = 0  # Initialize total to 0

    most_steps = []  # Initialize most_steps list to empty
    least_steps = []  # Initialize least_steps list to empty

    m_steps = 0  # Initialize m_steps to 0
    l_steps = 0  # Initialize l_steps to 0

    # Create list holding the days of the week
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Print message describing program
    print("You will be entering the number of steps taken for each day in a week.")

    for day in days:  # Loop through each day in days list
        day_steps = int(input("Please enter the number of steps taken on " + day + ": "))  # Get days_steps for day
        steps[day] = day_steps  # Add entry to steps dictionary using day as key and days_steps as value
        total += day_steps  # Add day_steps to total
        m_steps = l_steps = day_steps  # Assign day_steps to m_steps and l_steps for initialization

    average = total / len(days)  # Divide total by the length of days list to get the average

    for k in steps:  # Loop through each key in steps dictionary
        if steps[k] > m_steps:  # Check if value for key is greater than m_steps
            most_steps = [steps[k], k]  # If so, assign most_steps list to value of key followed by key
            m_steps = steps[k]  # Assign value for key to m_steps
        elif steps[k] == m_steps:  # Check if value for key is equal to m_steps
            most_steps.append(k)  # If so, append key to most_steps list

    for k in steps:  # Loop through each key in steps dictionary
        if steps[k] < l_steps:  # Check if value for key is less than l_steps
            least_steps = [steps[k], k]  # If so, assign least_steps list to value of key followed by key
            l_steps = steps[k]  # Assign value for key to l_steps
        elif steps[k] == l_steps:  # Check if value for key is equal to l_steps
            least_steps.append(k)  # If so, append key to least_steps list

    print("\nYou walked a total of", format(total, ','), "steps during the week.")  # Print the total
    print("That was an average of", format(int(average), ','))  # Print the average

    # Print index 0 of most_steps list containing the steps
    print("The maximum steps you took were", format(most_steps[0], ','), "on:")
    for val in most_steps:  # Loop through each val in most_steps list
        if str(val).isalpha():  # Check if value to string is alpha
            print("----" + val)  # If so, print the val

    # Print index 0 of least_steps list containing the steps
    print("The minimum steps you took were", format(least_steps[0], ','), "on:")
    for val in least_steps:  # Loop through each val in least_steps list
        if str(val).isalpha():  # Check if value to string is alpha
            print("----" + val)  # If so, print the val


main()  # Call main function
