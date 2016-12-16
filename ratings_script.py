from bs4 import BeautifulSoup

import requests, json


all_ratings = []

#here is the URL to the browse painting pages
# total_pages = 0
# #total_pages = 0
# while total_pages = 0:
#lets ask requests to get that page

url = "http://www.wrestlescoop.com/information/raw-vs-nitro-ratings-war/"
print(url)

data_page = requests.get(url)


			#just let us know if that failed
if data_page.status_code != 200:
	print ("There was an error with", url)

				#we are storing the HTML of the page into the variable page_html using the .text attribute of the request result
page_html = data_page.text

				#now we are going to ask BS to parse the page
soup = BeautifulSoup(page_html, "html.parser")


bigtable = soup.find("tbody")


all_trs = soup.find_all("tr")


for a_tr in all_trs:

	date_field = a_tr.find("td", attrs={"width":"73"})
	if date_field != None:
		print(date_field.text)

		rawwwfpromotion = a_tr.find("td", attrs={"width":"203"})
		if rawwwfpromotion!= None:



			nitrowcwpromotion = a_tr.find("td", attrs={"width":"236"})
			if nitrowcwpromotion != None:
			

				all_ratings.append({"Date": date_field.text, "Raw Rating": rawwwfpromotion.text, "Nitro Rating" : nitrowcwpromotion.text})


		

with open('scraped_ratingsdata.json', 'w') as f:
	f.write(json.dumps(all_ratings,indent=4))