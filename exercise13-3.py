# Week 4 Exercise - 13-3
# YC - Jun 25, 2019

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verity_mode = ssl.CERT_NONE

# User input
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retreive data
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

def nexturl(pos, url):
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")

	tags = soup('a')
	for tag in tags:
		if pos == 1:
			url = tag.get('href', None)
			name = tag.contents[0]
			return url, name
		pos -= 1

while count > 0:
	url, name = nexturl(position, url)
	count -= 1

print(name)

