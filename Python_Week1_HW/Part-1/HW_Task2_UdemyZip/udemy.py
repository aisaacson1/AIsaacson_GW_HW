import os
import csv

udemy_csv = os.path.join("web_starter.csv")

title = []
price = []
subscribers = []
reviews = []
length = []
reviewpercent = []

        
with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # loop through
    for row in csvreader:
        
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        length.append(float(row[9].split(' ')[0]))
        reviewpercent.append(int(row[6])/int(row[5])*100)

zipped_data = zip(title, price, subscribers, reviews, length, reviewpercent) 

output_file = os.path.join("aaron_web_final.csv")

with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)
        
        writer.writerow(["Title","Price","Subscribers","Reviews","Length","Reviews Percent"])
        writer.writerows(zipped_data)