A=90
B=80
C=70
D=60
F=60


#Get the test score from the user.
score = int(input('Enter the test score:'))

#Determinr the grade.
if score>=A:
    print('Score A ')
else:
    if score>=B:
        print('Score B ')
    else:
        if score>=C:
            print('Score C ')
        else:
           if score>=D:
                  print('Score D ')
           else:
                  print('Score F ')
           


#if-elif-else statement

#if score >= A:
    #print('Your grade is A.')
#elif score >= B:
    #print('Your grade is B.')
#elif score >= C:
    #print('Your grade is C.')
#elif score >= D:
    #print('Your grade is D.')
#else:
    #print('Your grade is F.') 
