# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []


# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = (row["first_name"] + "." + row["last_name"] + "@data.com")
        empdatadict = {"First Name":row["first_name"], "Last Name":row["last_name"], "SSN":row["ssn"], "Email":email}
        new_employee_data.append(empdatadict)

# Grab the filename from the original path
#_, filename = os.path.split(filepath)

# Write updated data to csv file
output = os.path.join("aaron_email_final.csv")

#csvpath = os.path.join("output")
with open(output, "w", newline='') as datafile:
        fieldnames = ['First Name', 'Last Name', 'SSN', 'Email']
        writer = csv.DictWriter(datafile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_employee_data)
    