# Program5_25(hypotenuse)
# This program calculate the lenght of a right
# triangle's hypotenuse.

import math
def main():
    # Get the lenght of the triangle's two sides.
    a=float(input('Enter the lenght of side A: '))
    b=float(input('Enter the lenght of side B: '))

    # Calculate the lenght of the hypotenuse.
    c=math.hypot(a,b)

    # Display the lenght of the hypotenuse.
    print('The lenght of the hypotenuse is',format(c,'.2f'))

# Call the main function.
main()


    
