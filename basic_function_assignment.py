"""
Author: Brady Trenary
Program: basic_function_assignment.py

Program takes an employee's name, hours worked, hourly wage and prints them.
"""


def hourly_employee_input():
    try:
        name = input('Enter employee name: ')
        hours_worked = int(input('Enter hours worked: '))
        hourly_pay_rate = float(input('Enter hourly pay rate: '))
        result = f'{name}, {hours_worked} hours worked, {hourly_pay_rate}/hr.'

        if name.isdigit():
            print('Invalid name input')
        elif hours_worked < 0 or hourly_pay_rate < 0:
            print("Invalid input")
        else:
            print(result)

    except ValueError:
        print('Invalid input')


if __name__ == '__main__':
    hourly_employee_input()
