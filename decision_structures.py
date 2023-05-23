"""Chapter 03 Assessment Program Logic - Decision Structures

Assignment Requirements:
For this assignment, you will be providing the logic (plan) for the following program:

You are writing a program to sell tickets to the school play. If the person buying the tickets is a student,
their price is $5.00 per ticket. If the person buying the tickets is a veteran, their price is $7.00 per ticket.
If the person buying the ticket is a sponsor of the play, the price is $2.00 per ticket.
If the person buying the ticket is a part of the public, the price is $10.00.

In addition, quantity discounts apply.
"""

STUDENT_PRICE = 5
VETERAN_PRICE = 7
SPONSOR_PRICE = 2
RETIREE_PRICE = 6
PUBLIC_PRICE = 10

LOW_DISCOUNT = .1
MEDIUM_DISCOUNT = .15
HIGH_DISCOUNT = .2

print("Play prices by ticket category:")
print("1. Student", "$" + format(STUDENT_PRICE, '.2f'))
print("2. Veteran", "$" + format(VETERAN_PRICE, '.2f'))
print("3. Sponsor", "$" + format(SPONSOR_PRICE, '.2f'))
print("4. Retiree", "$" + format(RETIREE_PRICE, '.2f'))
print("5. Public", "$" + format(PUBLIC_PRICE, '.2f'))

ticket_category = int(input("\nEnter the number of the ticket category you fit under for purchasing tickets"
                            " (Please enter a number between 1 and 5): "))

"""Check if the number entered is between 1 and 5"""
if 1 <= ticket_category <= 5:
    """If so set the ticket price"""
    if ticket_category == 1:
        ticket_price = STUDENT_PRICE
    elif ticket_category == 2:
        ticket_price = VETERAN_PRICE
    elif ticket_category == 3:
        ticket_price = SPONSOR_PRICE
    elif ticket_category == 4:
        ticket_price = RETIREE_PRICE
    else:
        ticket_price = PUBLIC_PRICE

    number_of_tickets = int(input("How many tickets would you like to purchase?: "))

    """Calculate the ticket cost"""
    cost_after_discounts = cost_before_discounts = ticket_price * number_of_tickets

    """Check that a valid number was entered"""
    if number_of_tickets != 0:
        """Check if a discount applies"""
        if 4 <= number_of_tickets <= 8:
            cost_after_discounts = cost_before_discounts - cost_before_discounts * LOW_DISCOUNT
        elif 9 <= number_of_tickets <= 15:
            cost_after_discounts = cost_before_discounts - cost_before_discounts * MEDIUM_DISCOUNT
        elif number_of_tickets > 15:
            cost_after_discounts = cost_before_discounts - cost_before_discounts * HIGH_DISCOUNT
        else:
            print("\nYou do not qualify for a ticket discount")

        """Calculate the price per ticket"""
        price_per_ticket = cost_after_discounts / number_of_tickets

        """If a ticket discount applies"""
        if cost_before_discounts != cost_after_discounts:
            print("\nYou qualify for a ticket discount")
            print("Your purchase total:", "$" + format(cost_before_discounts, '.2f'))
            print("Your purchase after discounts applied:", "$" + format(cost_after_discounts, '.2f'))
        else:
            print("Your purchase total:", "$" + format(cost_before_discounts, '.2f'))

        print("Your purchase is", "$" + format(price_per_ticket, '.2f'), "per ticket")
    else:
        print("\nYou entered an invalid number of tickets")
else:
    print("\nYou entered an invalid ticket category number")
