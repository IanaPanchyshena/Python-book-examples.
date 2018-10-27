# This program qualify whether the bank customer
# qualify for a loan

def main():
    Min_salary=30000.0   # The min annual salary 
    Min_years=2          # The min years on the current job

    #Get the annual salary
    salary=float(input('Enter you annual salary '))
    #Get the number of years on job
    years_job=int(input('Enter the number of years on current job '))

    #Determine whether the customer qualifies
    if salary>=Min_salary and years_job>=Min_years:
        print('You qualify for the loan ')
    else:
        print('You do not qualify for this loan ')

main()
