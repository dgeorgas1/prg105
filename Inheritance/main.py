import inheritance_classes


def main():  # Define main
    shift = 0  # Initialize shift

    # Ask for value for each attribute
    print("Please Enter Employee Data")
    employee_name = input("Name: ")

    while True:
        try:  # Try to convert value to int
            employee_number = int(input("ID Number: "))
            break
        except ValueError:
            print("Please Enter Only Numbers")

    while True:
        try:  # Try to convert value to int
            shift_number = int(input("Shift (1=day, 2=night, 0=unassigned): "))

            # If successful, check if value is equal to 1, 2 or 0
            while shift_number != 1 or shift_number != 2 or shift_number != 0:
                if shift_number == 1:
                    shift = "day"
                    break
                elif shift_number == 2:
                    shift = "night"
                    break
                elif shift_number == 0:
                    shift = "unassigned"
                    break
                else:
                    print("An invalid shift number was entered")
                    shift_number = int(input("Shift (1=day, 2=night, 0=unassigned): "))
            break
        except ValueError:
            print("Please Enter Only Numbers")

    while True:
        try:  # Try to convert value to float
            hourly_pay_rate = float(input("Hourly Pay Rate: "))
            break
        except ValueError:
            print("Please Enter Only Numbers")

    # Create instance object of ProductionWorker class setting the attributes
    production_worker = inheritance_classes.ProductionWorker(employee_name, employee_number, shift, hourly_pay_rate)

    # Get the values for printing
    print(f'\nEmployee: {production_worker.get_employee_number()} {production_worker.get_employee_name()}\n'
          f'Shift: {production_worker.get_shift_number()}\nPay Rate: ${production_worker.get_hourly_pay_rate()} per '
          f'hour')


main()  # Call main
