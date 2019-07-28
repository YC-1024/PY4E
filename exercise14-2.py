# Week 5 Exercise - 14.2
# YC - Jul 14, 2019
import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = False
# api_key = 'Input here is you have a Google Places API key'

if api_key is False:
	api_key = 42
	serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
	serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
	address = input('Enter location: ')
	if len(address) < 1: break

	parms = dict()
	parms['address'] = address
	if api_key is not False: parms['key'] = api_key
	print('Retrieving ', address)
	uh = urllib.request.urlopen(address, context=ctx)

	data = uh.read()
	print('Retrieved ', len(data), 'characters')

	info = json.loads(data)
	print('Count: ', len(info['comments']) )

	s = 0
	for e in info['comments']:
		s = s + int(e['count'])
	print('Sum: ', s)

