# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:39:03 2017
@author: cesar
2520 is the smallest number that can be divided by each of the numbers
 from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""
#check only prime numbers. create a gen. with multiples for 9699690
def gen_19():
    a=9699690
    while True:
        yield(a)
        a=a+9699690

#list with primes up to 20. Use generator and check %. returnlist
#with remainders

aa=gen_19()

def check_mult():
#    l=[2,3,5,7,11,13,17,19]
    l=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    nmbr=next(aa)
    nlist=[]
    for i in l:
        nlist.append(nmbr%i)
    return(nmbr, nlist)

#while loop until sum(list)=0

if __name__=='__main__':
                         
    while True:                  
        (n,chklst)=check_mult()
        if sum(chklst)==0:
            print('found multiple for {}'.format(n))
            break
        else:
            print('checking {}'.format(n))
                     