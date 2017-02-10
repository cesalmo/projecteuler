# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:09:42 2017
@author: Cesar Alvarez
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10 001st prime number?
"""
def prime_counter(n):
    '''give the first n prime numbers
    '''
    import p03_2
    gen=p03_2.eratosthenes()
    count=0
    while count < n:
        b=next(gen)
        count+=1
    return(b)

if __name__=='__main__':
    print(prime_counter(10001))