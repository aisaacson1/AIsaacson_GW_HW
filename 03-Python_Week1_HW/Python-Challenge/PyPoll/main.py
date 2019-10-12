# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:29:06 2019

@author: Aaron
"""

import pandas as pd

file_one = "Resources/election_data.csv"

file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")

title = "Election Results\n \n------------------------"
print(title)

#Find Total Votes
total_votes = file_one_df["Voter ID"].value_counts()
total_votes_str = (f"Total Votes: {sum(total_votes)} \n------------------------\n")
print(total_votes_str)

#Group candidates
grouped_candidates = file_one_df.groupby(["Candidate"])

#Get total votes per candidate
vote_p_can = grouped_candidates["Voter ID"].count()

#Find vote percent per candidate
p_votes = 100 * vote_p_can / total_votes.count()
pd.options.display.float_format = '{:.3f}%'.format

#create new DF with vote percent and total per candidate
voter_sum = pd.DataFrame({"Percent of Vote": p_votes, "Votes per Candidate": vote_p_can})
voter_sum = voter_sum.sort_values("Votes per Candidate", ascending=False)
voter_sum_str = (voter_sum.rename_axis('').rename_axis("Candidate", axis=1))
print(voter_sum_str)

#find Winner!
winner = vote_p_can.idxmax()
winner_str = (f"\n------------------------\nWinner: {winner}\n------------------------")
print(winner_str)

#print to txt doc
pypoll_text = open("PyPolling_Analysis.txt", "w")
L = [title, total_votes_str, voter_sum_str, winner_str]
for x in L:
    pypoll_text.write(str(x))
    pypoll_text.write("\n")
    
pypoll_text.close()