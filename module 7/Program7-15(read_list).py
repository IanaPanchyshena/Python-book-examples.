# Program7-15(read_list)

# This program reads a file's contents into a list.

def main():
    # Open a file for reading.
    infile=open('cities.txt','r')

    # Read the contents of the file into a list.
    cities=infile.readlines()

    # Close the file.
    infile.close()

    # Strip the \n from each elelment.
    index=0
    while index<len(cities):
        cities[index]=cities[index].rstrip('\n')
        index+=1

    # Print the context of the list.
    print(cities)

# Call the main function.
main()
