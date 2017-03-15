# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:09:03 2017
@author: Cesar Alvarez

In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def coins_count(Target,Coins):
    
    if Target == 0:
        return(1)
    if Target < 0 :
        return(0)
    if len(Coins)==0:
        return(0)   
   
    return( coins_count(Target, Coins[0:-1]) + coins_count(Target-Coins[-1], Coins))      

if __name__=='__main__':
    Coins=[1,2,5,10,20,50,100,200]
    Target=20
    print(coins_count(Target, Coins))