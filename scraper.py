######################################################################
# File name: scraper.py                                  	  
# Author: PhilipBasaric                                 			  
#                                                                     
# Description:   				  
#																	  										  
#																	      
#                                                                     
######################################################################

import requests
import re
import time 
import random
import pandas as pd 

class WebScraper:

	@staticmethod
	def apiRequest():
		api_version = "3"
		api_base_url = f"https://ckan0.cf.opendata.inter.prod-toronto.ca/api/{api_version}"
		endpoint_path = f"action/package_show"
		endpoint = f"{api_base_url}{endpoint_path}"
		params = { "id": "6e19a90f-971c-46b3-852c-0c48c436d1fc"}

		package = requests.get(endpoint, params = params).json()

		return package

	# The following function retrieves demographic data from a given city 
	#Argument(s): name of city (string)
	#Return(s): Pandas data frame containing demographic data 
	@staticmethod
	def getDemographics():
		package = apiRequest()

		for idx, resource in enumerate(package["result"]["resources"]):

			if resource["datastore_active"]:
				url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/datastore_search"
				p = { "id": resource["id"] }
				data = requests.get(url, params = p).json()
				df = pd.DataFrame(data["result"]["records"])
				break
		df
