# An implementation of the CoinGecko API that aims to be simpler and easier to understand
# By Henry Chedd and Amy(@00p513-dev)
# Licensed under the Don't Be A Dick Public License 

import json
import requests


#######################################################
# Check if you can connect to CoinGecko API           #
# Returns an array with connection result in index 0, #
# and api response in index 1                         #
#######################################################

def connectionTest():
	connected = False
	while not connected:
		r = requests.get('https://api.coingecko.com/api/v3/ping/')
		if r.status_code == 200:
			data = r.text
			jdata = json.loads(data)
			connected = True
			return [True, jdata['gecko_says']]
		else:
			try:
				data = r.text
				jdata = json.loads(data)
				return [False, jdata]
			except:
				return [False, 'Failed to recieve API data']

#######################################################
# Get price for one unit of crypto in a fiat currency #
#######################################################

def getCoinValue(crypto, fiat):
	url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=" + fiat + "&ids=" + crypto
	s = requests.get(url)
	if s.status_code == 200:
		data = s.text
		jdata = json.loads(data)
		return jdata[0]['current_price']

########################################
# Covvert fiat in to a crypto currency #
########################################

def convertToCrypto(crypto, fiat, amount):
	url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=" + fiat + "&ids=" + crypto
	s = requests.get(url)
	if s.status_code == 200:
		data = s.text
		jdata = json.loads(data)
		conversionRate = jdata[0]['current_price']
		price = amount*conversionRate
		return price

########################################
# Covvert crypto in to a fiat currency #
########################################

def convertToFiat(crypto, fiat, amount):
	url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=" + fiat + "&ids=" + crypto
	s = requests.get(url)
	if s.status_code == 200:
		data = s.text
		jdata = json.loads(data)
		conversionRate = jdata[0]['current_price']
		price = amount/conversionRate
		return price

######################################
# List of supported currencies       #
# Pretty version prints on new lines #
######################################

def supportedVsCurrencies():
	url = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
	s = requests.get(url)
	if s.status_code == 200:
		data = s.text
		jdata = json.loads(data)
		return jdata

def supportedVsCurrenciesPretty():
	supported = supportedVsCurrencies()
	supported = ', '.join(supported)
	return supported
