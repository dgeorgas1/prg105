"""Chapter 08 Practice 2 Program - Rainfall

Assignment Requirements:
Download this start file for rainfall:

rainfall-totals.txtDownload rainfall-totals.txt

Import the data from the file. Check to see if the data is valid, if it is not valid, indicate to the user
what the bad data is. Total and average the data, and display formatted results on the screen."""


def main():  # Define main function
    count = 0  # Initialize count to 0
    total = 0  # Initialize total to 0
    with open("rainfall-totals.txt", "r") as file:

        for line in file:  # Iterate through each line of file
            string = line.split()  # Split line to separate month from rainfall amount and assign to string

            # Split string for position 1 holding the rainfall amount at the decimal and assign to amount
            amount = string[1].split('.')
            amount = amount[0]  # Assign position 0 holding the whole number for rainfall amount to amount

            if amount.isnumeric():  # Check if amount is numeric
                try:
                    # If so, try to convert string for position 1 holding the amount to float and add to total
                    total += float(string[1])
                    count += 1  # Add 1 to count
                except ValueError:  # If unable to convert to float
                    # Print message bad numeric data found for entry: month and amount with a new line
                    print("Bad numeric data found for entry:", string[0], string[1], "\n")
            else:  # If amount is not numeric
                print(amount, "is not a number")  # Print message amount is not a number

    average = total / count  # Divide total by count and assign to average

    print(f"{count} good values were found.")  # Print the count of good values found
    print(f"The total was {total:.1f}.")  # Print the total formatting to 1 decimal place
    print(f"The average was {average:.1f}.")  # Print the average formatting to 1 decimal place


main()  # Call main function
