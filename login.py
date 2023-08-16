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
from colours import Color

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
                print(Color.GREEN + "login successful..."+ Color.RESET)
                print(Color.GREEN + "displaying Menu..."+ Color.RESET)
                subprocess.run(["/usr/bin/python3", "homepage.py"])
                return 0
            elif instance.email != email and instance.password != password:
                print(Color.RED + "status, status number, email or password is incorrect"+ Color.RESET)
                print(Color.YELLOW +"suggesting recover details"+ Color.RESET)
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
                print(Color.RED + "This email {} is incorrect!".format(email)+ Color.RESET)
                print(Color.YELLOW +"re-enter email again..."+ Color.RESET)
                email = input("Enter your email: ")
            else:
                print(Color.RED +"This password {} is incorrect!".format(password)+ Color.RESET)
                print(Color.YELLOW +"re-enter password again..."+ Color.RESET)
                password = input("Enter your password: ")
        elif status.lower() == "no":
            data = read_employee_data_from_file()
            instance = data[status_number - 1]
            if instance.email == email and instance.password == password:
                print(Color.GREEN +"login successful..."+ Color.RESET)
                print(Color.GREEN +"displaying Menu..."+ Color.RESET)
                subprocess.run(["/usr/bin/python3", "homepage.py"])
                return 0
            elif instance.email != email and instance.password != password:
                print(Color.RED +"status, status number, email or password is incorrect"+ Color.RESET)
                print(Color.YELLOW +"suggesting recover details"+ Color.RESET)
                choice = input("do you want to recover details yes or no: ")
                if choice.lower() == "yes":
                    print("Enter number for forgot detail in shell menu and \
returning to Menu.")
                    break
                else:
                    print(Color.YELLOW +"re-enter deatils again..."+ Color.RESET)
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    status = input("Enter yes for emloyer no for employee: ")
                    status_number = int(input("Enter your employee \
or employer number: "))
            elif instance.email != email:
                print(Color.RED +"This email {} is incorrect!".format(email)+ Color.RESET)
                print(Color.YELLOW +"re-enter email again..."+ Color.RESET)
                email = input("Enter your email: ")
            else:
                print(Color.RED +"This password {} is incorrect!".format(password)+ Color.RESET)
                print(Color.YELLOW +"re-enter password again..."+ Color.RESET)
                password = input("Enter your password: ")
        else:
            print(Color.RED +"Incorrect status enter yes or no..."+ Color.RESET)
            status = input("Enter your status again: ")
    return 1


outcome = login()
if outcome == 1:
    print(Color.RED +"Login Failure."+ Color.RESET)
else:
    print(Color.GREEN +"logging out."+ Color.RESET)
