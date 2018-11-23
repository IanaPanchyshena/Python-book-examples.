# Program7-13(writelines)

# This program uses the writelines method to save
# a list of strings to a file.

def main():
    # Create a list of strings.
    cities=['New York', 'Boston', 'Atlanta', 'Dallas']

    # Open a file for writting.
    outfile=open('cities.txt','w')

    # Write the list to the file.
    outfile.writelines(cities)

    # Close the file.
    outfile.close()

# Call the main function.
main()
