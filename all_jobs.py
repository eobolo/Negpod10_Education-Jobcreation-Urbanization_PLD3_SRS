#!/usr/bin/python3
"""
This script reads and

write a json file storing

all jobs in a dictionary
"""


import json


def read_json_file():
    try:
        with open("jobs.json", mode="r", encoding="utf-8") as JF:
            return json.load(JF)
    except FileNotFoundError:
        return {}

def write_json_file(job_data):
    with open("jobs.json", mode="w", encoding="utf-8") as JF:
        json.dump(job_data, JF)
    return 0
