# Program6-23(gross_pay)

# This program calculates gross pay.

def main():
    try:
        # Get the number hours worked.
        hours=int(input('Enter many hours did you work? '))

        # Get the hourly pay rate.
        pay_rate=float(input('Enter your hourly pay rate: '))

        # Calculate the gross pay.
        gross_pay=hours*pay_rate

        # Dispplay the gross pay.
        print('Gross pay:$',format(gross_pay,'.2f'),sep='')
    except ValueError:
        print('ERROR: Hours worked and hourly pay rate must')
        print('be valid numbers.')

# Call the main function.
main()
