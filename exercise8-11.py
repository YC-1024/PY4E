#Exercise 8.4
fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    words = line.split()
    for w in words:
        if not w in lst:
            lst.append(w) 
lst.sort()
print(lst)

#Exercise 8.5
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            print(words[1])
            count += 1

print("There were", count, "lines in the file with From as the first word")

#Exercise 9.4
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = {}

for lines in handle:
    if not lines.startswith('From'): continue
    words = lines.split()
    if len(words) < 3: continue
    counts[words[1]] = counts.get(words[1],0) + 1

maxmail = None
maxcount = 0
for k, v in counts.items():
    if maxmail == None or v > maxcount:
        maxmail, maxcount = k, v

print(maxmail, maxcount)

#Exercise 10.2
import re

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = {}

for line in handle:
    if re.search('^From.+[0-9]\S+:\S+[0-9]:\S+[0-9]', line):
        word = line.split()
        for w in word:
            if re.search('[0-9]\S+:\S+[0-9]:\S+[0-9]', w):
                h = w.split(':')[0]
                counts[h] = counts.get(h,0) + 1
                                
lst = list(counts.items())
lst.sort()
'''
for k, v in list(counts.items()):
    lst.append((v, k))
print (lst)
lst.sort(reverse=True)
'''
for k, v in lst:
    print (k, v)


# Exercise 11
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