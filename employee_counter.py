#!/usr/bin/python3
import pickle


def read_employee_counter_from_file():
    try:
        with open("employees_counter.txt", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return 0


def write_employee_counter_to_file(data):
    with open("employees_counter.txt", "wb") as file:
        pickle.dump(data, file)
