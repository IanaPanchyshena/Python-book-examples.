# user_squares2_4_11

# Thsi program uses a loop to display a
# table of numbers and their squares.

def main():

    TAX_FACTOR=0.0065
    
    # Get the starting value.
    print('This program displays a list of numbers')
    print('and their squares.')
    start=int(input('Enter the starting number: '))

    # Get the ending limit.
    end=int(input('How high should I go? '))

    # Print the headings.
    print()
    print('Numbers\tSquares')
    print('----------------')

    # Print the numbers and their squares.
    for number in range (start, end+1):
        square=number**2
        print(number,'\t',square)
main()
