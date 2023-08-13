#!/usr/bin/python3
"""
This helps update

details of employer

or employee.
"""


from employees import Employees
from employee_data import *
from employers import Employers
from employer_data import *


def update_details():
    print("Are you an Employer or Employee?")
    question = input("Enter yes for employer no for employee: ")
    while True:
        message = input("Enter yes for employer no for employee: ")
        if message.lower() == "yes":
            employer_num = int(input("Enter your employee number in digit: "))
            employer = read_employer_data_from_file()
            employer_instance = employer[employer_num - 1]
            print("What do you want to update?")
            message = input("age, name, email, phonenumber, \
dob(date of birth), password: ")
            if message.lower() == "age":
                data = input("Enter new age in number: ")
                employer_instance.age = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "name":
                data = input("Enter new name: ")
                employer_instance.name = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "email":
                data = input("Enter a new email: ")
                employer_instance.email = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "dob":
                data = input("Enter a new dob: ")
                employer_instance.dob = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "phonenumber":
                data = input("Enter new phonenumber: ")
                employer_instance.phnum = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "password":
                data = input("Enter new password: ")
                employer_instance.password = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            else:
                print(f"Entered wrong input {message}.")
                print("age, name, email, phonenumber, dob(date of birth), \
password are the options")
        elif message.lower() == "no":
            employee_num = int(input("Enter your employee number in digit: "))
            employee = read_employee_data_from_file()
            employee_instance = employee[employee_num - 1]
            print("What do you want to update?")
            message = input("age, name, email, phonenumber, \
dob(date of birth), password: ")
            if message.lower() == "age":
                data = input("Enter new age in number: ")
                employee_instance.age = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "name":
                data = input("Enter new name: ")
                employee_instance.name = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "email":
                data = input("Enter a new email: ")
                employee_instance.email = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "dob":
                data = input("Enter a new dob: ")
                employee_instance.dob = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "phonenumber":
                data = input("Enter new phonenumber: ")
                employee_instance.phnum = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            elif message.lower() == "password":
                data = input("Enter new password: ")
                employee_instance.password = data
                print("Do you still want to update profile?")
                message = input("Enter yes or no: ")
                if message.lower() == "yes":
                    continue
                else:
                    break
            else:
                print(f"Entered wrong input {message}.")
                print("age, name, email, phonenumber, dob(date of birth), \
password are the options")
        else:
            print(f"wrong input {message} Enter yes for employer no \
for employee.")

    if question.lower() == "yes":
        employer[employer_num - 1] = employer_instance
        write_employer_data_to_file(employer)
    else:
        employee[employee_num - 1] = employee_instance
        write_employee_data_to_file(employee)


update_details()
