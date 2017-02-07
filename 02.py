# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:51:06 2017

@author: cesar
"""

def F():
    a,b = 0,1
    while True:
        a, b = b, a + b
        yield b

gen=F()

#%%
n=0
while n<10:
    print(next(gen))
    n+=1

#%%
gen=F()

n=0
su = 0
while n < 4000000:
    if n%2 == 0:
        su = su + n
        print(su)
        n=next(gen)
    else:
        n=next(gen)