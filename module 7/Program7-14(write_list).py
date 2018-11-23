# Program7-14(write_list)

# This program saves a list of strings to a file.

def main():
    # Create a list of strings.
    cities=['New York', 'Boston', 'Atlanta', 'Dallas']

    # Open a file for writting.
    outfile=open('cities.txt','w')

    # Write the list to the file.
    for item in cities:
        outfile.write(item+'\n')
        
    # Close the file.
    outfile.close()

# Call the main function.
main()
