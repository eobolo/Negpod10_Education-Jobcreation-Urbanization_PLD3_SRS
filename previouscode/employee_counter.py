#!/usr/bin/python3
"""
This file creates the read
and write employee counter functions
for saving the employer counter

"""
import pickle



def read_employee_counter_from_file():
    """
    The reading function
    for the employer count
    """
    try:
        with open("employees_counter.txt", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return 0


def write_employee_counter_to_file(data):
    """
    The writing function
    for the employer count
    """
    with open("employees_counter.txt", "wb") as file:
        pickle.dump(data, file)
