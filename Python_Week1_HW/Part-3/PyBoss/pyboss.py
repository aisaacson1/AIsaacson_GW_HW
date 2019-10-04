# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:33:02 2019

@author: Aaron
"""
import pandas as pd 

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#open file and create DF
file_one = "employee_data.csv"
file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")


#Split name column into first and last
new_df = file_one_df["Name"].str.split(" ", n=1, expand = True)
file_one_df["First Name"]= new_df[0]
file_one_df["Last Name"]= new_df[1]
file_one_df.drop(columns =["Name"], inplace= True)

#set employee ID as index
#file_one_df.reset_index(drop=True, inplace=True)
#file_one_df.set_index("Emp ID")

#convert date format
file_one_df["DOB"] = pd.to_datetime(file_one_df.DOB)
file_one_df["DOB"] = file_one_df["DOB"].dt.strftime('%m/%d/%Y')

#mask SSN
file_one_df["SSN"] = file_one_df["SSN"].apply(lambda x: "***-**" + x[6:])

#convert state to abb
file_one_df["State"] = file_one_df["State"].map(us_state_abbrev)

#organize columns
file_one_df = file_one_df[["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]]

#sort on EMP ID
file_one_df = file_one_df.sort_values("Emp ID")

print(file_one_df.head())

#export to csv
file_one_df.to_excel("new_employee_data.xlsx", index=False)