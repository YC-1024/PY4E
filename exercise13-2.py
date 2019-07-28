# Week 4 Exercise - 13-2
# YC - Jun 24, 2019

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verity_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all anchor tags
'''
tags = soup('table')
print(tags)
for tag in tags:
	# Look at the parts of a tag
	print('TAG: ', tag)
	print('URL: ', tag.get('href', None))
	print('Contents: ', tag.contents[0])
	print('Attrs: ', tag.attrs)
'''

# Retrieve table
result = 0
span = soup("span")
for s in span:
	result += int(s.contents[0])
print(result)


