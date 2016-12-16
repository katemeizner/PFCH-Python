# PFCH-Python
Programming for Cultural Heritage - Monday Night Wars Project

"Monday Night Wars: Data From Wrestling's Golden Age" is a project that uses python programming and data visualization techniques to unpack an era of professional wrestling called "Monday Night Wars." 

"Monday Night Wars" references a six year ratings battle between two TV shows: World Championship Wrestling’s (WCW) Monday Night Nitro, and World Wrestling Federation’s (WWF) flagship show Monday Night Raw. The ratings war was part of an overall struggle between the two companies, which was perpetuated by personal feuding between WCW owner Ted Turner and WWF commissioner Vince McMahon. Competition between the two companies revolutionized the industry's approach to talent relations, character building, and storylines by forcing promotions to identify profitable markets and approach new extremes to meet viewer expectations.

I scraped my data from a wrestling database from Cagematch.com and wiki site called Wrestlescoop.com in hopes that I would be able identify trends that align with the historical details of the "Monday Night Wars" era. The data from Cagematch pertained to wrestling matches, and included match dates, locations, participants, titles, and the affiliated wrestling promotion. The data from Wrestlescoop.com details WWF Raw and WCW Nitro's show ratings from 1995 to 2001. 

Below, you will find instructions on how to scrape the data with Python, write the data to a JSON file, and finally, write the JSON files to CSVs.

Match Data:
1) Run each python script that begins with "projectscript_". You do not need to run them in order, but it is easiest to run all of the scripts ending in "_WCW" first, then all of the scripts ending in "_WWF" (it's easier to stay organized that way). Because Cagematch only return 1000 search results for each query, I had to use multiple scripts that scraped the data in small  batches of <1000 rows. 
2) Running all of the WCW scripts will scrape WCW wrestling match data and write it to a JSON file. After you've run each of the "_WCW" scripts, consolidate the WCW JSON files into one JSON filing by copy/pasting. Do the same with WWF data.
3) Consolidate the WCW and WWF JSON files into one all-inclusive JSON file using copy/paste. 
4) To create an edge table for import into Gephi, run "jsontocsv_edgetable.py", which parses JSON match data to a CSV.
5) To create a CSV of wrestling match data to import into Tableau, run "allmatches_jsontocsv.py"
Note: There are multiple iterations of each CSV because I had to clean the data in Google Refine.

Ratings Data:
1) Run "ratings_script.py" to scrape ratings data and write it to a JSON file.
2) Run "ratingsjsontocsv.py" JSON file to write JSON file to a CSV. 




