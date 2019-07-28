# PY4E - Course 3 - Access Web Data
# Exercise 10
# YC - May 30, 2019

import re

fname = input('Input file name: ')

try:
	fh = open(fname)
	fc = fh.read()
except:
	print('Invalid file!')
	quit()

text = re.findall('\d+' , fc)
num = list(map(int, text))

print(sum(num))

