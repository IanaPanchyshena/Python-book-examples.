# retail_with_validation4_16
# This program calculates retail prices.

def main():
    mark_up=2.5  #markup percentage
    another='y'  # Variable to control the loop

    # Process one or more items.
    while another=='y' or another=='Y':
        # Get the items wholesale cost.
        wholesale=float(input('Enyter the items wholesale cost: '))

        # Validate the wholesale cost.
        while wholesale <0:
            print('ERROR')
            wholesale=float(input('Enter the correct wholesale cost: '))
        #Calculate the retail price.
        retail=wholesale*mark_up

        #Dispaly the retail price.
        print('Retail price: $',format(retail,',.2f'),sep='')

main()
