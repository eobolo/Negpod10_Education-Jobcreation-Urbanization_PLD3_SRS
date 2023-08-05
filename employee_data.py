#!/usr/bin/python3
import pickle


def read_employee_data_from_file():
    try:
        with open("employees_data.txt", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def write_employee_data_to_file(data):
    with open("employees_data.txt", "wb") as file:
        pickle.dump(data, file)
