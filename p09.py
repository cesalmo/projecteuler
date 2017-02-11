# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:55:44 2017
@author: Cesar Alvarez
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
#with wolfram alpha:
    #solve a2+b2 = c2 and a+b+c=1000 and 414<c<500 and 292<b<500 and 0<a<293
#0<a<293
#b=(-500000+1000*a)/(-1000+a)
#c=(1000-a-b)

ls=[]
for a in range(1,294):
    b=(-500000+1000*a)/(-1000+a)
    c=(1000-a-b)
    ls.append([a,b,c])
    
print(ls[199][0]*ls[199][1]*ls[199][2])