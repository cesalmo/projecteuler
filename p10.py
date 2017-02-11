# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 23:08:56 2017
@author: Cesar Alvarez
"""
from p03_2 import eratosthenes

gen=eratosthenes()
sumat=0
n=0
while True:
    if int(n)<2000000:
        sumat=n+sumat
        n=next(gen)
    else:
        break
print(sumat)   