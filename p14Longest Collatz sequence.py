# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:56:16 2017
@author: Cesar Alvarez
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time

def large_sum(n):
    '''large_sum(n) n=number to start iteration
    yield(n,iteration)'''
    it = 1
    yield(n,it)
    while True:    
        if n%2==0 and n>2:
            n/=2
            it+=1
            yield(n,it)
        
        elif n%2!=0 and n>2:
            n=3*n+1
            it+=1
            yield (n,it)
        
        elif n<=2:
            n/=2
            it+=1
            yield(n,it)
            break


#%%
range_start=800000
range_end=900001

dict_comp = {1:1}
for a in range(range_start,range_end):
    print('iter n{}. time {}'.format(a,time.asctime()))    
#populate list with numbers and iterations and then we keep updating it.
#it is our memory to end up iterations when a number is found in this list.

    
    dict01 = {}
    for a,b in large_sum(a):
        if dict_comp.get(int(a)) == None:
            dict01[int(a)]=b
        else:
            dict01[int(a)]=b
            break
    
    l = dict01[sorted(dict01,key=dict01.get)[-1]] -dict01[sorted(
            dict01,key=dict01.get)[0]]
    
    #reversed list
    dict01_rev = {sorted(dict01,key=dict01.get,reverse=True)[i-1]:i-1
                  for i in range(1,l+2)} 
    
    plus = dict_comp[sorted(dict01_rev,key=dict01.get,reverse=True)[0]]
    
    #offset to match reversed list with dict_comp-
    for i,j in dict01_rev.items():
        dict01_rev[i] = j+plus
    
    dict_comp.update(dict01_rev)
    
dict_final = {a:b for a,b in dict_comp.items() if a <= range_end} #sorted from 100 down
print('terms ',dict_final.get(sorted(dict_final,key=dict_final.get)[-1]))
print('number ',sorted(dict_final,key=dict_final.get)[-1])
