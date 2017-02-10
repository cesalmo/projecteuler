# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:27:22 2017

@author: cesar
"""
l=[]
i=0

#for i in range(0,1000):
#    if i%3 == 0 or i%5 == 0:
#        l.append(i)
#
#print(sum(l))

print(sum(i for i in range(0,1000) if i%3 == 0 or i%5 == 0))
