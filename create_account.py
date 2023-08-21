#!/usr/bin/python3
from employees import Employees
from employers import Employers
from employer_data import *
from employee_data import *
from employee_counter import *
from employer_counter import *
from all_jobs import *
from colours import Color

def creating_login_details():

    """This is a function that gets
    our login details by using the keys
    and the values which are user's information
    and returns the user information as value list
    and the prompt as key.
    """

    # keys for login details
    keys = ["name", "email", "password", "dob", "phnum",
            "age", "status", "jobtitle"]

    # creating the login details
    values = list()

    # checking if user creating account is an employer or employee
    status = input("Enter Yes for employer and No for employee: ")
    # getting the details from the user and appending to the value list
    name = input("Enter your full-name: ")
    values.append(name)
    email = input("Enter your email address: ")
    values.append(email)
    password = input("Enter your password: ")
    values.append(password)
    date_of_birth = input("Enter your date-of-birth: ")
    values.append(date_of_birth)
    phone_number = int(input("enter your phone number without country code: "))
    values.append(phone_number)
    age = int(input("Enter your age in numbers: "))
    values.append(age)
    jobtitle = input("Enter your job title: ")
    values.append(status)
    values.append(jobtitle)
    return (keys, values, status, jobtitle)


def create_user_data():

    """This creates the user's data either for an employer
    or an employee based on the status given from the
    create login details and stores it in their
    repective data
    """
    # creating the employer and employee dict separately
    employees_dict = dict()
    employers_dict = dict()

    # get the values, keys, status
    keys, values, status, jobtitle = creating_login_details()

    # checking the status to assign to the correct dictionary
    if status.lower() == "yes":
        for key, value in zip(keys, values):
            employers_dict[key] = value

        # helps read data from employers file
        # and returns an empty list is no file is found
        # and if found returns the string containing our
        # employer list in list structure so we can append another
        employers = read_employer_data_from_file()
        counter = read_employer_counter_from_file()
        # appends new employer data to the employers list
        employers.append(Employers(counter, **employers_dict))
        counter = Employers.counter_return()
        # read the data back to the employer file
        write_employer_data_to_file(employers)
        write_employer_counter_to_file(counter)
        #saves the jobtitle of only employers
        #since only employers are the job givers
        job_data = read_json_file()
        job_names = jobtitle.split(sep=" ")
        job = ""
        for i in range(len(job_names)):
            if  i == len(job_names) - 1:
                job += job_names[i].capitalize()
                break
            elif i != len(job_names) - 1:
                job += job_names[i].capitalize() + " "

        if job[0] in job_data:
            job_data[job[0]].append(job)
        else:
            job_data[job[0]] = [job]
        print(job_data)
        write_json_file(job_data)
        # test if file is always saved
        print(employer_test())
        print(Color.GREEN +"Your employer number is {}.".format(counter)+ Color.RESET)
    else:
        for key, value in zip(keys, values):
            employees_dict[key] = value

        # helps read data from employees file
        # and returns an empty list is no file is found
        # and if found returns the string containing our
        # employee list in list structure so we can append another
        employees = read_employee_data_from_file()
        counter = read_employee_counter_from_file()
        # appends new employee data to the employees list
        employees.append(Employees(counter, **employees_dict))
        counter = Employees.counter_return()
        # read the data back to the employer file
        write_employee_data_to_file(employees)
        write_employee_counter_to_file(counter)
        # test if file is always saved
        print(employee_test())
        print(Color.GREEN +"Your employee number is {}.".format(counter)+ Color.RESET)


def employer_test():
    """This check if the data is updated
    for the employer
    """
    test = read_employer_data_from_file()
    return test


def employee_test():
    """This check if the data is updated
    for the employee
    """
    test = read_employee_data_from_file()
    return test


create_user_data()
