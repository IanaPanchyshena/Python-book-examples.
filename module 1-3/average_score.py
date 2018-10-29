#This program gets three scores and displays
#their average. It congrats the user if the
#average is a high score.


    
    
# The HIGH_SCORE named constant holds the value is
# considered a high score.
HIGH_SCORE = 95

# Get the three test scores
test1=int(input('Enter the score for tets1: '))
test2=int(input('Enter the test score for test2: '))
test3=int(input('Enter the test score for test3: '))

# Calculate the average
average=(test1+test2+test3)/3

#Print the average
print('The average score is',average)

#If the average is high score
# congratulate the user.
if average>=HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')
