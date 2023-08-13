#!/usr/bin/python3
"""
This module helps

search for jobs

save the job or

apply.
"""


from employees import Employees
from employee_data import *


read_json_file = __import__("all_jobs").read_json_file


def jobSearch():
    """
    function searches for

    jobs then ask if user wants

    to save the job, after listing it
    """
    while True:
        first_letter = input("give me first letter of the job: ")
        if first_letter.lower():
            first_letter = first_letter.upper()        
        data = read_json_file()
        if first_letter not in data:
            print(f"No letter {first_letter} matches this search")
            q_a = input("Do you want to still search? yes or no: ")
            if q_a.lower() == "yes":
                continue
            else:
                break
        get_job = data[first_letter]
        for i in range(len(get_job)):
            print(f"{get_job[i]}", end=", ")
        job_name = input("what job do you want to select: ")
        job_name = job_name.split(sep=" ")
        job = ""
        for i in range(len(job_name)):
            if  i == len(job_name) - 1:
                job += job_name[i].capitalize()
                break
            elif i != len(job_name) - 1:
                job += job_name[i].capitalize() + " "
        if job in get_job:
            print(job)
        outcome = input("Do you want to save the job: ")
        number = int(input("Give me your employee number: "))
        if outcome == "yes":
            print("Note you can only save one job, so apply before \
saving another.")
            employees = read_employee_data_from_file()
            employee = employees[number - 1]
            employee.jobsaved = job
            print(employee.jobsaved)
            employees[number - 1] = employee
            write_employee_data_to_file(employees)
            applying = input("Do you want to apply for the job, yes or no: ")
            if applying.lower() == "yes":
                print("Apply feature not implemented yet!")
                boolean = input("Do you want to stop searching yes or no: ")
                if boolean.lower() == "no":
                    continue
                else:
                    break
            boolean = input("Do you want to stop searching yes or no: ")
            if boolean.lower() == "no":
                pass
            else:
                break

        else:
            boolean = input("Do you want to stop searching yes or no: ")
            if boolean.lower() == "no":
                pass
            else:
                break

        """
        Now what to next

        1. ask user if he want to save or not
        2. then either saving or not
        3. that is when user wanting to continue searching is asked
        4. now add the savedjobs attribute for employee class, job title
           for employee and employer class, and give it setter and getter
           for the savedjobs attribute.

        """
    return 0
jobSearch()
