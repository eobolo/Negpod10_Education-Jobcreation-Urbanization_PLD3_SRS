#!/usr/bin/python3
# login.py
"""This is the login
file that helps create
that helps user login
"""


from employees import Employees
from employee_data import *
from employers import Employers
from employer_data import *
import subprocess


def login():
    """function that helps login
    askes for email, password,
    employee/employer number
    status(employee or employer)
    """
    print("Enter login details.")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    status = input("Enter yes for emloyer no for employee: ")
    status_number = int(input("Enter your employee or employer number: "))
    while True:
        if status.lower() == "yes":
            data = read_employer_data_from_file()
            instance = data[status_number - 1]
            if instance.email == email and instance.password == password:
                print("login successful...")
                print("displaying Menu...")
                subprocess.run(["/usr/bin/python3", "homepage.py"])
                return 0
            elif instance.email != email and instance.password != password:
                print("status, status number, email or password is incorrect")
                print("suggesting recover details")
                choice = input("do you want to recover details yes or no: ")
                if choice.lower() == "yes":
                    print("Enter number for forgot detail in shell menu and \
returning to Menu.")
                    break
                else:
                    print("re-enter details again...")
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    status = input("Enter yes for emloyer no for employee: ")
                    status_number = int(input("Enter your employee \
or employer number: "))
            elif instance.email != email:
                print("This email {} is incorrect!".format(email))
                print("re-enter email again...")
                email = input("Enter your email: ")
            else:
                print("This password {} is incorrect!".format(password))
                print("re-enter password again...")
                password = input("Enter your password: ")
        elif status.lower() == "no":
            data = read_employee_data_from_file()
            instance = data[status_number - 1]
            if instance.email == email and instance.password == password:
                print("login successful...")
                print("displaying Menu...")
                subprocess.run(["/usr/bin/python3", "homepage.py"])
                return 0
            elif instance.email != email and instance.password != password:
                print("status, status number, email or password is incorrect")
                print("suggesting recover details")
                choice = input("do you want to recover details yes or no: ")
                if choice.lower() == "yes":
                    print("Enter number for forgot detail in shell menu and \
returning to Menu.")
                    break
                else:
                    print("re-enter deatils again...")
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    status = input("Enter yes for emloyer no for employee: ")
                    status_number = int(input("Enter your employee \
or employer number: "))
            elif instance.email != email:
                print("This email {} is incorrect!".format(email))
                print("re-enter email again...")
                email = input("Enter your email: ")
            else:
                print("This password {} is incorrect!".format(password))
                print("re-enter password again...")
                password = input("Enter your password: ")
        else:
            print("Incorrect status enter yes or no...")
            status = input("Enter your status again: ")
    return 1


outcome = login()
if outcome == 1:
    print("Login Failure.")
else:
    print("logging out.")
