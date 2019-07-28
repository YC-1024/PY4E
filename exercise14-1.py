# Week 5 Exercise - 14.1
# YC - Jun 26, 2019
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# api_key = 'Input here is you have a Google Places API key'

if api_key is False:
	api_key = 42
	serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	parms = dict()
	parms['address'] = address
	if api_key is not False: parms['key'] = api_key
	# url = serviceurl + urllib.parse.urlencode(parms)
	print('Retrieving ', address)
	uh = urllib.request.urlopen(address, context=ctx)

	data = uh.read()
	print('Retrieved ', len(data), ' characters')
	# print(data.decode())
	tree = ET.fromstring(data)

	commentlist = tree.findall('.//comment')
	print('Count: ', len(commentlist))
	#lat = results[0].find('geometry').find('location').find('lat').text

	result = 0
	for e in commentlist:
		result += int(e.find('count').text)
	
	print('Sum: ', result)

