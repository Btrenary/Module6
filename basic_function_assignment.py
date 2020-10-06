"""
Author: Brady Trenary


"""

def hourly_employee_input():
    name = input('Enter employee name: ')
    hours_worked = int(input('Enter hours worked: '))
    hourly_pay_rate = float(input('Enter hourly pay rate: '))
    result = f'{name}, {hours_worked} hours worked, {hourly_pay_rate}/hr.'
    if hours_worked < 0 or hourly_pay_rate < 0:
        print("Invalid input")
    
    else:
        print(result)


hourly_employee_input()



