#!/usr/bin/python3
# homepage.py
"""This is our home page
for our users where, jobs
can be searched and applied
for, your profile can be updated
read private policy, and
log out.
"""


import time


def messages():
    message1 = "Welcome to Jobify"
    message2 = "The home of connecting Employers to Employees and"
    message3 = "Vice-versa."
    option1 = "Press 1 to apply for job."
    option2 = "Press 2 to search for job."
    option3 = "Press 3 to update profile."
    option4 = "Press 4 to log out."
    print("{:^135}".format(message1))
    print("{:^135}".format(message2))
    print("{:^133}".format(message3))
    print("{:^133}".format(option1))
    print("{:^135}".format(option2))
    print("{:^135}".format(option3))
    print("{:^128}".format(option4))

"""
def options():
    message = "Enter your option here: "
    print("{:^110}".format(message))
    while True:
        option = int(input())
        if option == 1:
            print("Feature in development")
            print("Enter 4 to log out")
        elif option == 2:
            print("Working in progress (WIP).")
            print("Enter 4 to log out")
        elif option == 3:
            print("Coming Soon.")
            print("Enter 4 to log out")
        elif option == 4:
            try:
                raise SystemExit("Preparing to log out.")
            except SystemExit as systemexit:
                print(systemexit)
                time.sleep(3)
            break
        else:
            print("Option {} not Available, put correct option"
                  .format(option))
"""

"""
def homepage():
    """This is the homage function
    it has a bit of GUI(graphical
    user interface) for the users
    to enjoy with options with some
    features in-development, beta
    version and so on.
    """
    # Display messages in code GUI format
    messages()
    options()
"""

homepage()
