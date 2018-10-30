# property_tax4_13
# This program displays property taxes.

def main():

    TAX_FACTOR=0.0065

    # Get the first lot number.
    print('Enter the property lot number')
    print('or enter 0 to end.')
    lot=int(input('Lot number: '))

    # Continue processing as long as the user
    # does not enter lot number 0.
    while lot !=0:
        # Get the property value.
        value=float(input('Enter the property value: '))

        # Calculate the property's tax.
        tax=value*TAX_FACTOR

        # Display the tax.
        print('Property tax: $',format(tax,'.2f'),sep='')

        # Get the next lot number.
        print('Enter the next lot number or')
        print('enter 0 to end.')
        lot=int(input('Lot number: '))

main()

