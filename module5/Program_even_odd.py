# Program_even_odd

def main():
    
    number=int(input('Enter a number: '))
    if is_even(number):
        print('The number is even.')
    else:
        print('The number is odd.')

def is_even(number):
            if(number%2)==0:
                status=True
        
            else:
                status=False

main()
