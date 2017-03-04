# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:12:24 2017
@author: Cesar Alvarez
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28
 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
 n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
 number that can be written as the sum of two abundant numbers is 24.
 By mathematical analysis, it can be shown that all integers greater than 28123
 can be written as the sum of two abundant numbers. However, this upper limit 
 cannot be reduced any further by analysis even though it is known that the 
 greatest number that cannot be expressed as the sum of two abundant numbers 
 is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
 of two abundant numbers.
"""
import time
starttime = time.time()

amic=__import__('p21Amicable numbers')
#limits
upperlimit=28124
lowerlimit=1
#create list with abundant numbers
abundantlist=list(a for a in range (lowerlimit,upperlimit) if sum(amic.factors(a)) > a)
abundantset=set(abundantlist)
#list with int which can be written as sum
newset=set()
for a in range(lowerlimit,upperlimit):
    for b in abundantlist:
        if (a in newset) == False:
            if ((a-b) in abundantset) == True:
                newset.add(a)
#opposite list
newset2=set()
for a in range(lowerlimit,upperlimit):
    if (a in newset) == False:
        newset2.add(a)
#print
print('sumatory={}'.format(sum(newset2)))
print(time.time() - starttime)     