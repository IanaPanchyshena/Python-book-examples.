# Program6-5(strip_newline)

# This program reads the contents of the
# philosophers.txt file one line at the time.

def main():
    # Open file named pholosophers.txt.
    infile=open('philosophers.txt','r')

    # Read three lines from the file.
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()

    # Strip the \n from each string.
    line1=line1.rstrip('\n')
    line2=line2.rstrip('\n')
    line3=line3.rstrip('\n')

    # Close the file.
    infile.close()

    # Print the data that was read into memory.
    print(line1)
    print(line2)
    print(line3)

# Call the main function.
main()

    
