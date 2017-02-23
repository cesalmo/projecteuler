# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:52:26 2017
@author: Cesar Alvarez
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name 
score.
For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
import time
starttime = time.time()
#from functools import reduce
#import list
with open('p22_names.txt','r') as file:
    listnames=file.read()
listnames=listnames.replace(r'"',r'').split(',')
#create dict with names
dictnames=dict(enumerate(sorted(listnames),1))
#create dict with char values
charvalues={chr(a):a-64 for a in range(65,91)}

print('sumatory={}'.format(sum([a*sum(list((charvalues[c] for c in dictnames[a].strip()))) for a,b
in dictnames.items()])))

print('time={}'.format(time.time() - starttime))