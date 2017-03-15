# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:21:51 2017
@author: Cesar Alvarez
Surprisingly there are only three numbers that can be written as the sum of 
fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.

"""

Limit=355000
start=10
acum=0
for j in range(start,Limit):
    a=list(str(j))
    b=[int(i)**5 for i in a]
    
    if sum(b) == j:
        print('number={}'.format(j))
        acum+=j
        print('acummulator={}'.format(acum))