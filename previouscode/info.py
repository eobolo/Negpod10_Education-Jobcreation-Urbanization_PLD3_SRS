#!/usr/bin/python3
from employer_data import *
from employers import Employers
from employee_data import *
from employees import Employees

employer = read_employer_data_from_file()
employee = read_employee_data_from_file()
print(employer[0].email)
print(employee[0].email)
print(employee[0].counter, employer[0].counter)
print(employee[0].status, employer[0].status)
