import json

with open('scraped_ratingsdata.json', 'r') as json_file:
    text = json_file.read()
    data = json.loads(text)

    #print(data)

ratingscsv = []

for a_row in data:
    matchdate = a_row['Date']
    nitrorating = a_row['Nitro Rating']
    rawrating = a_row['Raw Rating']
        
    ratingscsv.append([matchdate, nitrorating, rawrating])

import csv
with open('promotionratings.csv', 'w') as fp:
    csvwriter = csv.writer(fp, delimiter=",")
    csvwriter.writerows(ratingscsv)
