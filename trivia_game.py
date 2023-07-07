"""Chapter 10 Practice 2 Program - Trivia Game

Assignment Requirements:
In this programming exercise, you will create a simple trivia game for two players. The program will work like this:

Starting with player 1, each player gets a turn at answering 5 trivia questions. (There should be a total of 10
questions.) When a question is displayed, 4 possible answers are also displayed. Only one of the answers is correct,
and if the player selects the correct answer, he or she earns a point.
After answers have been selected for all the questions, the program displays the number of points earned by each
player and declares the player with the highest number of points the winner.
To create this program, write a Question class to hold the data for the trivia question. The question class should
have attributes for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.

The program should have a list or a dictionary containing 10 Question Objects, one for each trivia question. Make up
your own trivia question on the subject or subjects of your choice for the objects."""


class Question:
    # Define initializer method
    def __init__(self, question=0, answer_1=0, answer_2=0, answer_3=0, answer_4=0, correct_answer=0):
        self.__question = question
        self.__answer_1 = answer_1
        self.__answer_2 = answer_2
        self.__answer_3 = answer_3
        self.__answer_4 = answer_4
        self.__correct_answer = correct_answer

    # Define set_question mutator method
    def set_question(self, question):
        self.__question = question

    # Define set_answer_1 mutator method
    def set_answer_1(self, answer_1):
        self.__answer_1 = answer_1

    # Define set_answer_2 mutator method
    def set_answer_2(self, answer_2):
        self.__answer_2 = answer_2

    # Define set_answer_3 mutator method
    def set_answer_3(self, answer_3):
        self.__answer_3 = answer_3

    # Define set_answer_4 mutator method
    def set_answer_4(self, answer_4):
        self.__answer_4 = answer_4

    # Define set_correct_answer mutator method
    def set_correct_answer(self, correct_answer):
        self.__correct_answer = correct_answer

    # Define get_question accessor method
    def get_question(self):
        return self.__question

    # Define get_answer_1 accessor method
    def get_answer_1(self):
        return self.__answer_1

    # Define get_answer_2 accessor method
    def get_answer_2(self):
        return self.__answer_2

    # Define get_answer_3 accessor method
    def get_answer_3(self):
        return self.__answer_3

    # Define get_answer_4 accessor method
    def get_answer_4(self):
        return self.__answer_4

    # Define get_correct_answer accessor method
    def get_correct_answer(self):
        return self.__correct_answer


def main():  # Define main function
    count = 0  # Initialize count
    correct_answer = 0  # Initialize correct_answer
    question_number = 0  # Initialize question_number
    player1_score = 0  # Initialize player1_score
    player2_score = 0  # Initialize player2_score

    # Create an instance object of Question Class for each question
    question_1 = Question()
    question_2 = Question()
    question_3 = Question()
    question_4 = Question()
    question_5 = Question()
    question_6 = Question()
    question_7 = Question()
    question_8 = Question()
    question_9 = Question()
    question_10 = Question()

    # Set question, answer options and correct_answer for question_1
    question_1.set_question("What is a correct syntax to output \"Hello World\" in Python?:")
    question_1.set_answer_1("1. echo \"Hello World\"")
    question_1.set_answer_2("2. echo(\"Hello World\");")
    question_1.set_answer_3("3. p(\"Hello World\")")
    question_1.set_answer_4("4. print(\"Hello World\")")
    question_1.set_correct_answer(4)

    # Set question, answer options and correct_answer for question_2
    question_2.set_question("Which one is NOT a legal variable name?")
    question_2.set_answer_1("1. _myvar")
    question_2.set_answer_2("2. Myvar")
    question_2.set_answer_3("3. my-var")
    question_2.set_answer_4("4. my_var")
    question_2.set_correct_answer(3)

    # Set question, answer options and correct_answer for question_3
    question_3.set_question("What is the correct file extension for Python files?:")
    question_3.set_answer_1("1. .pt")
    question_3.set_answer_2("2. .pyth")
    question_3.set_answer_3("3. .pyt")
    question_3.set_answer_4("4. .py")
    question_3.set_correct_answer(4)

    # Set question, answer options and correct_answer for question_4
    question_4.set_question("What is the correct syntax to output the type of a variable or object in Python?:")
    question_4.set_answer_1("1. print(typeof(x))")
    question_4.set_answer_2("2. print(typeOf(x))")
    question_4.set_answer_3("3. print(typeof x)")
    question_4.set_answer_4("4. print(type(x))")
    question_4.set_correct_answer(4)

    # Set question, answer options and correct_answer for question_5
    question_5.set_question("Which method can be used to remove any whitespace from both the beginning and the end"
                            "of a string?:")
    question_5.set_answer_1("1. strip()")
    question_5.set_answer_2("2. trim()")
    question_5.set_answer_3("3. len()")
    question_5.set_answer_4("4. ptrim()")
    question_5.set_correct_answer(1)

    # Set question, answer options and correct_answer for question_6
    question_6.set_question("Which method can be used to return a string in upper case letters?:")
    question_6.set_answer_1("1. toUpperCase()")
    question_6.set_answer_2("2. upper()")
    question_6.set_answer_3("3. uppercase()")
    question_6.set_answer_4("4. upperCase()")
    question_6.set_correct_answer(1)

    # Set question, answer options and correct_answer for question_7
    question_7.set_question("Which method can be used to replace parts of a string?:")
    question_7.set_answer_1("1. replace()")
    question_7.set_answer_2("2. repl()")
    question_7.set_answer_3("3. switch()")
    question_7.set_answer_4("4. replaceString()")
    question_7.set_correct_answer(1)

    # Set question, answer options and correct_answer for question_8
    question_8.set_question("Which operator is used to multiply numbers?:")
    question_8.set_answer_1("1. X")
    question_8.set_answer_2("2. #")
    question_8.set_answer_3("3. %")
    question_8.set_answer_4("4. *")
    question_8.set_correct_answer(4)

    # Set question, answer options and correct_answer for question_9
    question_9.set_question("Which operator can be used to compare two values?:")
    question_9.set_answer_1("1. <>")
    question_9.set_answer_2("2. =")
    question_9.set_answer_3("3. ><")
    question_9.set_answer_4("4. ==")
    question_9.set_correct_answer(4)

    # Set question, answer options and correct_answer for question_10
    question_10.set_question("Which of these collections defines a LIST?:")
    question_10.set_answer_1("1. {\"name\": \"apple\", \"color\": \"green\"}")
    question_10.set_answer_2("2. [\"apple\", \"banana\", \"cherry\"]")
    question_10.set_answer_3("3. (\"apple\", \"banana\", \"cherry\")")
    question_10.set_answer_4("4. {\"apple\", \"banana\", \"cherry\"}")
    question_10.set_correct_answer(2)

    """Question 1"""
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_1_dict = question_1.__dict__  # Convert question_1 instance object to dictionary

    for k in question_1_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_1_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_1_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 2"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_2_dict = question_2.__dict__  # Convert question_2 instance object to dictionary

    for k in question_2_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_2_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_2_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 3"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_3_dict = question_3.__dict__  # Convert question_3 instance object to dictionary

    for k in question_3_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_3_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_3_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 4"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_4_dict = question_4.__dict__  # Convert question_4 instance object to dictionary

    for k in question_4_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_4_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_4_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 5"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_5_dict = question_5.__dict__  # Convert question_5 instance object to dictionary

    for k in question_5_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_5_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_5_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 6"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_6_dict = question_6.__dict__  # Convert question_6 instance object to dictionary

    for k in question_6_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_6_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_6_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 7"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_7_dict = question_7.__dict__  # Convert question_7 instance object to dictionary

    for k in question_7_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_7_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_7_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 8"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_8_dict = question_8.__dict__  # Convert question_8 instance object to dictionary

    for k in question_8_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_8_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_8_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 9"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_9_dict = question_9.__dict__  # Convert question_9 instance object to dictionary

    for k in question_9_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_9_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_9_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    """Question 10"""
    count = 0
    question_number += 1  # Add 1 to question_number

    current_player = get_player(question_number)  # Call get_player function
    question_10_dict = question_10.__dict__  # Convert question_10 instance object to dictionary

    for k in question_10_dict:  # Loop through keys
        if count < 5:  # Check if count is less than 5
            print(question_10_dict[k])  # If so, print value of key
            count += 1  # Add 1 to count
        else:  # If count is greater than or equal to 5
            correct_answer = question_10_dict[k]  # Assign value of key to correct_answer

    correct = check_answer(correct_answer)  # Call check_answer function

    if correct:
        if current_player == 1:  # Check if current_player is 1
            player1_score += 1  # If so, add 1 to player1_score
        else:  # If player2
            player2_score += 1  # Add 1 to player2_score

    get_results(player1_score, player2_score)  # Call get_results function


def get_player(question_number):  # Define get_player function
    if question_number % 2 == 1:  # Check if question_number is not divisible by 2
        print("It is players 1 turn")  # If so, print message It is players 1 turn
        current_player = 1  # Assign current_player to 1
    else:  # Divisible by 2
        print("It is players 2 turn")  # Print message It is players 2 turn
        current_player = 2  # Assign current_player to 2

    return current_player  # Return current_player


def check_answer(correct_answer):  # Define check_answer function
    while True:  # Loop to check answer
        try:  # Try to convert answer to int
            # Ask user for their answer
            answer = int(input("Please enter the number corresponding to the selected answer: "))
            break  # Break out of loop
        except ValueError:  # If unable to convert answer
            print("Error - You did not enter a number")  # Print message Error - You did not enter a number

    if answer == correct_answer:  # Check if answer is equal to correct_answer
        print("You got the question correct\n")  # If so, print message You got the question correct
        correct = True  # Assign correct to True
    else:  # Answer does not match
        print("You did not get the question correct\n")  # Print message You did not get the question correct
        correct = False  # Assign correct to False

    return correct  # Return correct


def get_results(player1_score, player2_score):  # Define get_results function
    print(f"Results\nPlayer 1: {player1_score}\nPlayer 2: {player2_score}")  # Print score for each player

    if player1_score > player2_score:  # Check if player1_score is greater than player2_score
        print("Player 1 wins")  # If so, print message Player 1 wins
    elif player2_score > player1_score:  # Check if player2_score is greater than player1_score
        print("Player 2 wins")  # If so, print message Player 2 wins
    else:  # Scores are equal
        print("It is a tie")  # Print message It is a tie


main()  # Call main function
