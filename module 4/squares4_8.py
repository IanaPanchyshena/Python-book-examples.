# squares4_8
# This program uses a loop to display a
# table showing the number 1 through 10
# and their squares.

def main():
    # Print the table headings.
    print('Number\tSquare')
    print('---------------')

    # Print the numbers 1 through 10
    # and their squares.
    for number in range(1,11):
        square=number**2
        print(number,'\t',square)
main()
