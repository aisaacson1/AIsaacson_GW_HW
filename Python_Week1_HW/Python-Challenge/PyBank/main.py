# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:28:27 2019

@author: Aaron
"""

import pandas as pd

file_one = "Resources/budget_data.csv"

file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")

title = "Financial Analysis \n ------------------------"
print(title)

#Find Total Months
total_months = file_one_df["Date"].value_counts()
total_months_str = (f"Total Months: {sum(total_months)}")
print(total_months_str)

#Find Total Earnings
net_total = file_one_df["Profit/Losses"].sum()
net_total_str = (f"Total: ${net_total}")
print(net_total_str)

#Find Average Change in Profits/Losses
file_one_df["change"] = file_one_df["Profit/Losses"].diff()
average_change = file_one_df["change"].mean()
average_change_str = (f"Total: ${round(average_change, 2)}")
print(average_change_str)

#Find Greatest Increase and Date
max_increase = file_one_df["change"].max()
idx_max = file_one_df["change"].idxmax()
max_increase_date = file_one_df.iloc[idx_max,0]
idx_max = file_one_df[file_one_df["Profit/Losses"]==max_increase].index
great_increase_str = (f"Greatest Increase in Profits: {max_increase_date} (${int(max_increase)})")
print(great_increase_str)

#Find Greatest Decrease and Date
min_decrease = file_one_df["change"].min()
idx_min = file_one_df["change"].idxmin()
min_decrease_date = file_one_df.iloc[idx_min,0]
idx_min = file_one_df[file_one_df["Profit/Losses"]==min_decrease].index
great_decrease_str = (f"Greatest Decrease in Profits: {min_decrease_date} (${int(min_decrease)})")
print(great_decrease_str)

pybank_text = open("Pybank_Analysis.txt", "w")
L = [title, total_months_str, net_total_str, average_change_str, great_increase_str, great_decrease_str]
for x in L:
    pybank_text.write(x + "\n")
    
pybank_text.close()