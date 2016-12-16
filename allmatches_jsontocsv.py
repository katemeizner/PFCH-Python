import json

wrestling_matches = []

with open('scrapedmatchdata_all.json', 'r') as json_file:
    text = json_file.read()
    data = json.loads(text)

    print(data)



#test = {
        #"promotion": "World Championship Wrestling",
        #"wrestlers": [
            # "Billy Kidman",
            # "Rey Mysterio Jr.",
            # "3-Count",
            # "Evan Karagias",
            # "Shannon Moore",
            # "The Jung Dragons",
            # "Kaz Hayashi",
            # "Yang"
        #],
    #     "match type": "WCW Cruiserweight Tag Team Title #1 Contendership Three Way: ",
    #     "event title": "WCW Monday NITRO #286 - Night Of Champions",
    #     "date": "26.03.2001",
    #     "location": " @ Panama City Beach, Florida, USA",
    #     "match card": "Billy Kidman & Rey Mysterio Jr. defeat 3-Count (Evan Karagias & Shannon Moore) and The Jung Dragons (Kaz Hayashi & Yang) (3:40)"
    # }

for a_row in data:
    matchdate = a_row['date']
    some_wrestlers = a_row['wrestlers']
    a_promotion = a_row['promotion']
    event_title = a_row['event title']
    event_location = a_row['location']
    wrestling_matches.append([matchdate, some_wrestlers, a_promotion, event_title, event_location])

import csv
with open('wrestlingmatches.csv', 'w') as fp:
    csvwriter = csv.writer(fp, delimiter=",")
    csvwriter.writerows(wrestling_matches)
