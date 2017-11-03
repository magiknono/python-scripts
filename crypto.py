#! python3

# crypto.py
# goal : Check quickly the last usd price of a crypto via terminal
# usage : python crypto.py [currencyname]
# note: api update every 5 minutes

# Steps :

import json, requests, sys, pprint

# Reads the requested ticker from the command line
if len(sys.argv) < 2:
  print('Usage: crypto.py currencyname')
  sys.exit()
ticker = ' '.join(sys.argv[1:])

# Download the JSON data from coinmarketcap.com
## api endpoint of ticker in default usd
url='https://api.coinmarketcap.com/v1/ticker/%s' % (ticker)
response = requests.get(url)
response.raise_for_status

# Convert the strings of JSON data to a python data structure
cryptoData = json.loads(response.text)

#Store data in a var
c= cryptoData[0]

# Prints the last price of a crypto and some stuff
## for json show : pprint.pprint(cryptoData)
print('Current price for %s:' % (ticker))
print('$ : %s' % (c['price_usd']))
print('percent change 24h : %s' % (c['percent_change_24h']))
print('percent change 7d : %s' % (c['percent_change_7d']))
