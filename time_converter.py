#Get the number of seconds from the user.
total_second=float(input('Enter a number of seconds: '))
#Get the number of hours.
hours=total_second//3600
#Get the number of remeining minutes
minutes=(total_second//60)%60
#Get the number of remainig seconds
seconds=total_second%60
#Display the result
print('Here is the time in hours,minutes,seconds: ')
print('Hours',hours)
print('Minutes',minutes)
print('Seconds',seconds)

                   
