#!/usr/bin/python3
# forgetdetails.py
"""This is a file
that manages the forget
login details part
"""


from employees import Employees
from employee_data import *
from employers import Employers
from employer_data import *


def forget_details():
    print("forgot details give me password: ")
    email = input("give me your correct email...: ")
    for object1 in read_employee_data_from_file():
        if object1.email == email:
            object1.employees_forget_details()
            return 0
    for object2 in read_employer_data_from_file():
        if object2.email == email:
            object2.employers_forget_details()
            return 0
    return 1


outcome = forget_details()
if outcome == 0:
    print("details gotten successfully...")
else:
    print("details not found, email incorrect or not found in database")
