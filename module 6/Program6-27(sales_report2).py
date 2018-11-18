# Program6-27(sales_report2)

# This program disolays the total of the
# amounts in the sales_data.txt file.

def main():
    # Initialize an accumulator.
    total=0

    try:
        # Open the sales.txt file.
        infile=open('sales_data.txt','r')

        # Read the values from the file and
        # accumulate them.
        for line in infile:
            amount=float(line)
            total+=amount

        # Close the file.
        infile.close()

        # Print the total.
        print(format(total,'.2f'))
    except:
        print('An error occured.')

# Call the main function.
main()


