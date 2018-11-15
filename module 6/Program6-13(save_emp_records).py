# Program6-13(save_emp_records)
# This program gets employee data from the user and
# saves it as resords in the employee.txt file.

def main():
    # Get the number of employee records to create.
    num_emps=int(inout('How many employee records'+
                       'do you want to create?'))
    # Open a file for writing.
    emp_file=open('employees.txt','w')

    # Get each employee'sdata and write it to the file.
    for count in range(1,num_emps+1):
        print('Enter data for employee #',count,sep='')
        name=input('Name: ')
        id_num=input('ID number: ')
        dept=input('Department: ')

        
