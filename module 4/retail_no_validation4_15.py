# retail_no_validation4_15

# This program calculates retail prices.

def main():
    mark_up=2.5 #markup percentage.
    another='y' #variable to control the loop.

    # Process one or more items.
    while another=='y' or another =='Y':
        # Get the items wholesale cost.
        wholesale=float(input('Enter the items wholesale cost: '))

        # Calculate theretail price.
        retail=wholesale*mark_up

        # Dispaly the retail price.
        retail=wholesale*mark_up

        # Display the retail price.
        print('Retail price:$',format(retail,',.2f'),sep='')

        # Do this again?
        another=input('Do you have another item?'+
                      '(Enter y for yes): ')

main()
