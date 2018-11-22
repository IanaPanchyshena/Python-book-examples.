# Program7-12(drop_lowest_score)

# Get the student’s test scores.
# Calculate the total of the scores.
# Find the lowest score.
# Subtract the lowest score from the total. This gives the adjusted total.
# Divide the adjusted total by 1 less than the number of test scores.
# This is the average.
# Display the average.

def main():
    scores=get_scores()
    total=get_total(scores)
    lowest=min(scores)
    total-=lowest
    average=total/(len(scores)-1)
    print('The average, with the lowest score dropped is',
          average)

def get_scores():
    test_scores=[]
    again='y'
    while again=='y':
        value=float(input('Enter a test score: '))
        test_scores.append(value)

        print('Do you want to add another score?')
        again=input('y=yes,n=no: ')
        print()
    return test_scores

def get_total(value_list):
    total=0
    for num in value_list:
        total+=num
    return total

main()
        
