#!/usr/bin/env python
"""ebay_scraper.py: This file reads ebay product data and writes it into csv format."""
__author__ = "Handell Desulme"

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from classes import details
import csv

website = 'https://www.ebay.com/b/' #Main Site
ending = '?LH_Sold=1&rt=nc&_pgn=' #URL Parameters
#Part 1 List: ['Baby-Clothing-Bottoms.260020.bn_7116417383','Baby-Toddler-Christening-Clothing.139762.bn_661887','Baby-Dresses.260021.bn_7116415533','Baby-One-Piece-Clothing.260022.bn_7116412592','Baby-Outerwear.260023.bn_7116391832','Baby-Outfits-Sets.260024.bn_7116419465','Baby-Skirts.260025.bn_7116418442','Baby-Sleepwear.260026.bn_7116411623','Baby-Socks-Tights.260027.bn_7116414542','Baby-Suits.260028.bn_7116417380','Baby-Sweaters.260029.bn_7116412595','Baby-Swimwear.260030.bn_7116391800','Baby-Clothing-Tops.260031.bn_7116399789','Baby-Underwear.260032.bn_7116398823']
#Part 2 List: ['Child-Car-Booster-Seats-up-to-80lbs.66694.bn_2310426','Baby-Car-Seat-Accessories.66693.bn_2311597','Convertible-Baby-Car-Seats-5-40lbs.66695.bn_2311519','Infant-Car-Seats-5-20lbs.66696.bn_2313806','Infant-Car-Seat-Head-Supports.117030.bn_2313993','Baby-Jumpers.117032.bn_2309908','Baby-Swings.2990.bn_2311142','Baby-Activity-Centers.20413.bn_2312159','Baby-Gyms-Play-Mats.19069.bn_2311328','Baby-Bouncers-Vibrating-Chairs.117034.bn_2310336','Baby-Play-Shades-Tents.117033.bn_2309941','Baby-Shopping-Cart-Covers.73470.bn_2310072','Baby-Safety-Gates.117029.bn_2311108','Toddler-Safety-Harnesses.134761.bn_2311464','Baby-Bed-Rails.162183.bn_2311017','Nursery-Mats-Rugs.37632.bn_2311343','Nursery-Mobiles.20429.bn_2310930','Cribs.2985.bn_2311394','Crib-Mattresses.117035.bn_2311576','Baby-Rockers-Gliders.66690.bn_2311061','Baby-Bedside-Sleepers.121152.bn_2310279','Bassinets-Cradles.20423.bn_2310732','Strollers.66700.bn_1865261','Stroller-Accessories.180911.bn_7203539','Stroller-Parts.121634.bn_7203525','Other-Strollers.2989.bn_7203492']
page_names = [] #<- Lists above go here

for page_name in page_names:
	item_count = 1; #csv row header
	for x in range(1,51): #first 50 pages
		my_url = website+page_name.replace('.','/')+ending+str(x)
		uClient = uReq(my_url)
		try: #Error is not properly handled.
			page_html = uClient.read()
		except (http.client.IncompleteRead) as e:
			continue #If the scraper breaks, adjust/update the page_names list and rerun it.
		uClient.close()

		page_soup = soup(page_html, "html.parser")
		ul =  page_soup.findAll("li", {"class":"s-item "}) #get all product list items

		#images = [] #div class:s-item__image-section

		listItems = []
		#listItem = details.Details() #div class:s-item__info clearfix

		for listItem in ul:
			
			#Store the element values that you need for each li
			url = listItem.a["href"]
			name = listItem.h3.text

				#Accessing spans require second soup call
			price = soup(str(listItem), "html.parser").find("span", class_="s-item__price").get_text()
			val = soup(str(listItem), "html.parser").find("span", class_="s-item__shipping")
			
				#Store shipping data if it's available
			if val is None:
				shipping = "N/A"
			else:
				shipping = val.get_text()
			
			val = soup(str(listItem), "html.parser").find("span", class_="s-item__dynamicAttributes1")
			
				#Access Dynamic Attributes
			if val is None:
				da1 = "N/A"
			else:
				da1 = val.get_text()
			val = soup(str(listItem), "html.parser").find("span", class_="s-item__dynamicAttributes2")
			if val is None:
				da2 = "N/A"
			else:
				da2 = val.get_text()
			val = soup(str(listItem), "html.parser").find("span", class_="s-item__dynamicAttributes3")
			if val is None:
				da3 = "N/A"
			else:
				da3 = val.get_text()
			
			#For terminal output
			listItem = details.Details(url, name, price, shipping, da1, da2, da3)
			print(str(item_count) + " " + listItem.__str__())
			print()
			print()

			#For csv output
			fileName = page_name+'.csv'
			if item_count == 1: #for header
				with open(fileName, 'w', newline = '') as csvFile:
					writer = csv.writer(csvFile)
					writer.writerow(listItem.getCSVHeader())
					writer.writerow(listItem.getCSVRow())
			else: #for remaining rows
				with open(fileName, 'a', newline = '') as csvFile:
					writer = csv.writer(csvFile)
					writer.writerow(listItem.getCSVRow())

			item_count = item_count + 1; #increment csv row









