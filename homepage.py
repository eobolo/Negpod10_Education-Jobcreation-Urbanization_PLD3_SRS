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
import subprocess
from colours import Color

def messages():
    message1 = "Welcome to Jobify"
    message2 = "The home of connecting Employers to Employees and"
    message3 = "Vice-versa.\n\n"
    option1 = "Press 1 to search, save, and apply for jobs as employee."
    option2 = "Press 2 to update profile either as employee or employer."
    option3 = "Press 3 to log out."
    print(Color.BLUE +"{:^135}".format(message1)+ Color.RESET)
    print(Color.BLUE +"{:^135}".format(message2)+ Color.RESET)
    print(Color.BLUE +"{:^133}".format(message3)+ Color.RESET)
    print("{:^134}".format(option1))
    print("{:^135}".format(option2))
    print("{:^98}".format(option3))


def options():
    message = "Enter your option here: "
    print("{:^102}".format(message))
    while True:
        option = int(input())
        if option == 1:
            subprocess.run(["/usr/bin/python3", "search&save.py"])
            print("\n\nEnter 1 to search, save and apply jobs\nEnter 2 \
to update profile,\nEnter 3 to log out.")
        elif option == 2:
            subprocess.run(["/usr/bin/python3", "update_details.py"])
            print("Enter 1 to search, save and apply jobs\nEnter 2 \
to update profile,\nEnter 3 to log out.")
        elif option == 3:
            try:
                raise SystemExit("Preparing to log out.")
            except SystemExit as systemexit:
                print(systemexit)
                time.sleep(3)
            break
        else:
            print(Color.RED + "Option {} not Available, put correct option"
                  .format(option)+Color.RESET)


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


homepage()
