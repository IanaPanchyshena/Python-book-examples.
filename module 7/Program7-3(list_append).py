# Program7-3(list_append)

# This program demonstrate how to append method
# can be used to add items to a list.

def main():
    # First, create an empty list.
    name_list=[]

    # Create variable to control the loop.
    again ='y'

    # Add some names to the list.
    while again=='y':
        # Get a name from the user.
        name=input('Enter a name: ')

        # Append the name to the list.
        name_list.append(name)

        # Add another one?
        print('Do you want to add another name?')
        again=input('y=yes,anything else=no: ')
        print()

    # Display the names that were entered.
    print('Here are the names you entered.')

    for name in name_list:
        print(name)

# Call the main function.
main()
