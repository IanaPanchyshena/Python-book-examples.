# Program5_11(keyword_args)

def main():
    # This program demonstrateof simple interest, using 0.01 as
    # interest rate per period, 10 as the number of perios,
    # and $10,000 as the principal.
    show_interest(rate=0.01,periods=10,principal=10000.00)

# The show_interest function displays the amount of
# simple interest for a given principal, interest rate
# per period, and number of periods.

def show_interest(principal,rate,periods):
    interest=principal*rate
    print('The simple interest will be $',
          format(interest,'.2f'),
          sep='')

# Call the main function.
main()

