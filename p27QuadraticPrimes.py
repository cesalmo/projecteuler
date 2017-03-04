# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:26:50 2017
@author: Cesar Alvarez
Euler discovered the remarkable quadratic formula:

n2+n+41n2+n+41
It turns out that the formula will produce 40 primes for the consecutive 
integer values 0≤n≤390≤n≤39. However, when 
n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and 
certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces 
80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the 
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

where |n||n| is the modulus/absolute value of nn
e.g. |11|=11|11|=11 and |−4|=4|−4|=4
Find the product of the coefficients, aa and bb, for the quadratic expression 
that produces the maximum number of primes for consecutive values of nn, 
starting with n=0n=0.
"""

import eulerlib
#prime list creation (below 1000000)
SieveGenerator=eulerlib.eratosthenes()
next(SieveGenerator)
PrimeDict={2: 1}
while True:
    NextPrime=next(SieveGenerator)
    if NextPrime>1000000:
        break
    PrimeDict[NextPrime]=1
    
#prime list creation (below 1000)
SieveGenerator=eulerlib.eratosthenes()
next(SieveGenerator)
bList=[2]
while bList[-1] <= 1000:
    bList.append(next(SieveGenerator))
bList.remove(bList[-1])


 
#for +-b in Primelist
#   for +- a < 1000
#       while n2+an+b in PrimeList: n+=1 


nMax=0
aMax=0
bMax=0
for b in bList:
    for a in range(-999,999):
        n=0
        while PrimeDict.get(n**2+a*n+b) == 1:
            n+=1
#            print(a,b,Result)
        if n>=nMax:
            nMax,aMax,bMax=n,a,b
            print(nMax,aMax,bMax,aMax*bMax)
            
        