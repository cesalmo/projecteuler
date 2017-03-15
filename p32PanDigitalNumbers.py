# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:42:33 2017
@author: Cesar Alvarez
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.
"""

import functools
import time
starttime = time.time()

# 10...99 * 100 ... 999
AcumSet=set()
for a in range(10,100):
#    print(a)
    for b in range (100,1000):
        product=a*b
        FinalList=list(map(int, list(str(product)+str(a)+str(b))))
        if sum(FinalList) == 45:
            if functools.reduce(lambda x,y: x*y, FinalList) == 362880:
                if len(FinalList)==9:
                    checklist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    if [checklist[d] in FinalList for d in range(0,9)] == [True,
                        True, True, True, True, True, True, True, True,]:
                        AcumSet.add(a*b)
   
# 1...9 * 1000 ... 9999      
for a in range(1,10):
#    print(a)
    for b in range (1000,10000):
        product=a*b
        FinalList=list(map(int, list(str(product)+str(a)+str(b))))
        if sum(FinalList) == 45:
            if functools.reduce(lambda x,y: x*y, FinalList) == 362880:
                if len(FinalList)==9:
                    checklist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    if [checklist[d] in FinalList for d in range(0,9)] == [True,
                        True, True, True, True, True, True, True, True,]:
                        AcumSet.add(a*b)
print(sum(AcumSet))
print('time={}'.format(time.time() - starttime))
       
        




