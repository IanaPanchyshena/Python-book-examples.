# gross pay4_14

# This program displays gross pay.

def main():
    # Get the number of hours worked.
    hours=int(input('Enter the hours worked this week: '))

    # Get the hourly pay rate.
    pay_rate=float(input('Enter the hourly pay rate: '))

    # Calculate the gross pay.
    gross_pay=hours*pay_rate

    # Displays the gross pay.
    print('Gross pay: $',format(gross_pay,',.2f'),sep='')

main()
