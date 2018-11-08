# Progrma5_20(coin_toss)

# This program demonstrates 10 tosses of a coin.
import random

HEADS=1
TAILS=2
TOSSES=10

def main():
    for toss in range (TOSSES):
        # Simulate the coin toss.
        if random.randint(HEADS,TAILS)==HEADS:
            print('Heads')
        else:
            print('Tails')

# Call the main function.
main()

    
