"""Chapter 03 Practice 1 Program - Financial Aid

Assignment:
You are writing a program to determine if a student is eligible for financial aid for the next semester.
To qualify, the student must either be a new student or a current student with a GPA of 2.0 or higher.
Additionally, the student may not have a criminal record for drugs
must enroll in a minimum of six credit hours of classes,
and must have a gross yearly income of less than $50,000.
You will gather information from the student,
and you will let them know if they are eligible for financial aid or not.

Hint: this is a bunch of different types of if statements, not an if-elif-else chain
"""

new_student = input("Are you a new or returning student? (Please enter n or r): ")

if new_student == 'r':
    current_student_gpa = float(input("Enter your GPA: "))
else:
    current_student_gpa = 0

criminal_record = input("Have you ever been convicted of a drug felony? (Please enter y or n): ")
enrolled_credit_hours = int(input("How many credit hours are you currently enrolled in for the semester?: "))
gross_yearly_income = int(input("Enter your gross yearly income (Please round to the nearest whole number): "))

if new_student == 'n' or current_student_gpa >= 2.0:
    if criminal_record == 'n':
        if enrolled_credit_hours >= 6:
            if gross_yearly_income < 50000:
                print("You are eligible for financial aid")
            else:
                print("You are not eligible for financial aid")
        else:
            print("You are not eligible for financial aid")
    else:
        print("You are not eligible for financial aid")
else:
    print("You are not eligible for financial aid")
