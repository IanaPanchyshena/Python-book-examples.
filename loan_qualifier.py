#This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY =30000.0 #The minimum annual salary
MIN_YEARS=2       #The minimum years on the job

# Get the customer's annual salary
salary=float(input('Enter your annual salary: '))

# Get the number of years on current job.
years_on_job=int(input('Enter the number of'+
                       'years employed: '))
# Determine whether the customer qualifies.
if salary>=MIN_SALARY:
    if years_on_job>=MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You maust have been employed',
              'for at least',MIN_YEARS,
              'yers to qualify.')
else:
            print('You must earn at least $',
                  format(MIN_SALARY,'.2f'),
                  ' per year to qualify.',sep='')
            
