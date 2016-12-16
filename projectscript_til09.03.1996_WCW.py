#1) the db only returns 1000 items, so how would I return all of them and add the lists together (04.09.1995 - 10.19.1998)
#2) I want a row for each wrestler so I can then make pairs for Gephi
#3) would like to leave championship info and match duration info in if i can

from bs4 import BeautifulSoup

import requests, json


all_matches = []

#here is the URL to the browse painting pages

url = "http://www.cagematch.net/?id=112&view=search&sEventName=WCW%20Monday%20Nitro&sEventType=TV-Show&sDateFromDay=04&sDateFromMonth=09&sDateFromYear=1995&sDateTillDay=19&sDateTillMonth=10&sDateTillYear=1998&sPromotion=2&sRegion=Amerika&sWorkerRelationship=Any&s="


total_pages = 0
while total_pages <= 10:
#lets ask requests to get that page

	
	print(url)

	data_page = requests.get(url)


				#just let us know if that failed
	if data_page.status_code != 200:
		print ("There was an error with", url)

					#we are storing the HTML of the page into the variable page_html using the .text attribute of the request result
	page_html = data_page.text

					#now we are going to ask BS to parse the page
	soup = BeautifulSoup(page_html, "html.parser")


	bigtable = soup.find("div", attrs = {"class":"TableContents"})


	all_trs = soup.find_all("tr", attrs = {"class":"TRow"})


	for a_tr in all_trs:

		date_field = a_tr.find("td", attrs={"class":"TCol TColSeparator"})
		if date_field != None:

			promotion = a_tr.find("img", attrs={"class":"ImagePromotionLogoMini"})
			if promotion!= None:

				matchtypes_span = a_tr.find("span", attrs={"MatchType"})
				if matchtypes_span != None:
					matchtypes = matchtypes_span.text
				else:
					matchtypes = ""

				event_span = a_tr.find("div", attrs={"class":"MatchEventLine"})
				if event_span != None:	

					show_title = event_span.find("a").text
					if show_title != None:

						location_title = event_span.text.replace(show_title,"")

						matchcard_span = a_tr.find("span", attrs={"class":"MatchCard"})
						if matchcard_span != None:
							wrestler_name = matchcard_span.find_all("a")
							if wrestler_name != None:
								wrestlername_list = []
								for a_name in wrestler_name:
									wrestlername_list.append(a_name.text)

				
								all_matches.append({"promotion": promotion['title'], "date": date_field.text, "match type" : matchtypes, "match card" : matchcard_span.text, "event title" : show_title, "location": location_title, "wrestlers": wrestlername_list})

	total_pages = total_pages + 1
	url = "http://www.cagematch.net/?id=112&view=search&sEventName=WCW%20Monday%20Nitro&sEventType=TV-Show&sDateFromDay=04&sDateFromMonth=09&sDateFromYear=1995&sDateTillDay=19&sDateTillMonth=10&sDateTillYear=1998&sPromotion=2&sRegion=Amerika&sWorkerRelationship=Any&s=" + str(total_pages * 100)

		

with open('scrapedmatchdata_til1996_WCW.json', 'w') as f:
	f.write(json.dumps(all_matches,indent=4))