# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:11:33 2017
@author: Cesar Alvarez
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

"""
import time
starttime = time.time()
def factors(n):
    #check natural numbers from 1 to sqr(n)
    #for every divisor i found, we get a i/n divisor
    fact=set()    
    for i in range(2,(int(n**0.5)+1)):
        if n%i==0:
            fact.add(1)
            fact.add(i)
            fact.add((n)//i)            
    return(fact)

if __name__=='__main__':
    n=10000 #set upper limit
    sumat=dict()
    for i in range(2,n):
        num=factors(i)
        sumat[i]=sum(num)
#filter dict for items<1000
    sumat2=[(b,a) for a,b in sumat.items() if b<n  ]
#compare items    
    amic=list()
    for a,b in sumat2:
        for c,d in sumat.items():
            if (a,b)==(c,d) and a!=b:
                print(a,b)
                amic.append(a)
    print('sumatory={}'.format(sum(amic)))
    print(time.time() - starttime)            