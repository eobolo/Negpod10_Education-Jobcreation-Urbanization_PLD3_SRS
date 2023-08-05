#!/usr/bin/python3
import pickle


def read_employer_data_from_file():
    try:
        with open("employers_data.txt", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


# def write_employer_data_to_file(data):
    # with open("employers_data.txt", "wb") as file:
        # pickle.dump(data, file)
