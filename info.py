#!/usr/bin/python3
from employer_data import *
from employers import Employers
from employee_data import *
from employees import Employees
import sys

employer = read_employer_data_from_file()
employee = read_employee_data_from_file()
print(employer[int(sys.argv[1]) - 1].email)
print(employer[int(sys.argv[1]) - 1].name)
print(employer[int(sys.argv[1]) - 1].password, employer[int(sys.argv[1]) - 1].dob)
print(employer[int(sys.argv[1]) - 1].age, employer[int(sys.argv[1]) - 1].phnum)
# print(employer[int(sys.argv[1]) - 1].jobsaved)
