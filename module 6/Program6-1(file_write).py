# Program6-1(file_write)
# This program writes three lines of data
# t a file.
def main():
    # Open a file named philosophers.txt.
    outfile=open('philosophers.txt', 'w')

    # Write the names of three philosophers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file.
    outfile.close()

# Call the main function.
main()
