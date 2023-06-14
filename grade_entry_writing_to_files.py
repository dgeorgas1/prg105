"""Chapter 07 Practice 1 Program - Grade Entry and Writing to Files

Assignment Requirements:
Ask the user how many students are in their class. Get the student's name and final grade. Store the answers in
a two-dimensional list, display the list, then write the list to the grades.txt file in a comma separated format
using quotes around the string values.

Tip-full-size-gold-1.png Hint: Use an f-string to format the file output, including the quotes and comma."""


def main():  # Define the main function
    student_grades = []  # Initialize student_grades list
    count = 0  # Initialize count

    number_of_students = int(input("How many students do you need to enter grades for?: "))  # Get number_of_students

    while count < number_of_students:  # Check if count is less than number_of_students
        student_name = input("Enter the name of student " + str(count + 1) + ": ")  # Get student_name
        grade = input("Enter the student's final letter grade: ")  # Get grade

        student_grades.append([student_name, grade])  # Append student_name and grade to student_grades list
        count += 1  # Add 1 to count

    print(student_grades)  # Print student_grades list

    current_student = 0  # Initialize current_student to 0
    current_grade = 0  # Initialize current_grade to 0

    file = open('grades.txt', 'w')  # Open grades.txt for writing

    while current_student < number_of_students:  # Check if current_student is less than number_of_students
        student_name = (student_grades[current_student][current_grade])  # Assign student_name index to student_name
        current_grade += 1  # Add 1 to current_grade
        grade = (student_grades[current_student][current_grade])  # Assign grade index to grade

        file.write(f"'{student_name}', '{grade}'\n")  # Write student_name and grade to file

        current_student += 1  # Add 1 to current_student
        current_grade = 0  # Assign current_grade to 0
    file.close()  # Close the file


main()  # Call main function
