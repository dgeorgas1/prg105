"""Chapter 03 Practice 2 Program - Credit Score

Assignment Requirements:
Ask your user for their credit score. Tell them if they have Bad, Fair, Good, or Excellent credit:
"""

credit_score = int(input("Enter your credit score (Please enter a score between 300 and 850): "))
credit_score_range = 0

if 300 <= credit_score <= 629:
    credit_score_range = "bad"
    print("Your credit score of", credit_score, "falls under", credit_score_range)
else:
    if 630 <= credit_score <= 689:
        credit_score_range = "fair"
        print("Your credit score of", credit_score, "falls under", credit_score_range)
    else:
        if 690 <= credit_score <= 719:
            credit_score_range = "good"
            print("Your credit score of", credit_score, "falls under", credit_score_range)
        else:
            if 720 <= credit_score <= 850:
                credit_score_range = "excellent"
                print("Your credit score of", credit_score, "falls under", credit_score_range)
