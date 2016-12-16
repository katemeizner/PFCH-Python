import json

wrestler_edges = []

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
    matchdate = matchdate[6: ]
    matchdate = int(matchdate)
    if matchdate > 1994 and matchdate < 2002:
        for wrestler_a in a_row['wrestlers']:
            for wrestler_b in a_row['wrestlers']:
                if wrestler_a != wrestler_b:
                    #print(wrestler_a, ",", wrestler_b)
                    wrestler_edges.append([wrestler_a, wrestler_b, "undirected", a_row['promotion'], matchdate])

import csv
with open('wrestler_edge_full_yeardate.csv', 'w') as fp:
    csvwriter = csv.writer(fp, delimiter=",")
    csvwriter.writerows(wrestler_edges)
