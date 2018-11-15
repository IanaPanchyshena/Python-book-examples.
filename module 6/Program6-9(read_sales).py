# Program6-9(read_sales)

# This program reads al of the values in
# the sales.txt file.

def main():
    # Open the sales.txt file for reading.
    sales_file=open('sales.txt','r')

    # Read the first line from the file, but
    # dont cinvert to a number yet. We still
    # need to test an empty string.
    line=sales_file.readline()

    # As long as an empty string is not returned
    # from readline, continue processing.
    while line!='':
        # Convert line to a float.
        amount=float(line)

        # Format and display the amount.
        print(format(amount,'.2f'))

        # Read the next line.
        line=sales_file.readline()

    #Close the file.
    sales_file.close()

# Call the main function.
main()
