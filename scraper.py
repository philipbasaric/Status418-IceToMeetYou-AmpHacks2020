######################################################################
# File name: scraper.py                                  	  
# Author: PhilipBasaric                                 			  
#                                                                     
# Description:   				  
#																	  										  
#																	      
#                                                                     
######################################################################

from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen
from urllib.request import urlretrieve
import wikipediaapi
from bs4 import BeautifulSoup
import requests
import re
import time 
import random
import pandas as pd 

class WebScraper:

	@staticmethod
	def apiRequest():
		article = articleName
		api_version = "rest_v1"
		api_base_url = f"https://wikimedia.org/api/{api_version}"
		endpoint_path = f"/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{article}/monthly/2015100100/2020060100"
		endpoint = f"{api_base_url}{endpoint_path}"

		r = requests.get(endpoint)

		data_dict = r.json()

		try:
			list_data = data_dict['items']
			return sortPopularLinks.getViews(list_data)
		except Exception as e:
			return 0

	# The following function retrieves demographic data from a given city 
	#Argument(s): name of city (string)
    #Return(s): 2D vector containing population data 
	@staticmethod
	def getDemographics(city):
		wikiUrl = "https://en.m.wikipedia.org/wiki/Demographics_of_" + city 

		try:
			html = urlopen(wikiUrl)
		except HTTPError as e:
			print('Page not found')
		except URLError as e:
			print('The server could not be found')
		else:
			print('Retrieval successful.')

		bs = BeautifulSoup(html.read(), 'html.parser')

		bs.find_all('table')

		df = pd.read_html((bs.find_all('table')))

		
