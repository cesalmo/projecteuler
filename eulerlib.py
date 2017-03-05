# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:15:15 2017
@author: Cesar Alvarez
"""
import functools
import itertools
#import time
#starttime = time.time()
#print('time={}'.format(time.time() - starttime))


#factorial
@functools.lru_cache(maxsize=None)
def fac(number):
    ''' factorial of a non-negative integer
    '''
    if number == 1:
        return 1
    number = number*fac(number-1)
    return number

#fibonacci

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

#erathostenes sieve


def eratosthenes( ):
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {  }  # map each composite integer to its first-found prime factor
    for q in itertools.count(2):     # q gets 2, 3, 4, 5, ... ad infinitum
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, so q is prime, therefore, yield it
            yield q
            # mark q squared as not-prime (with q as first-found prime factor)
            D[q*q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D:
                x += p
            D[x] = p

#prime counter
def prime_counter(n):
    '''give the first n prime numbers
    '''
    
    gen=eratosthenes()
    count=0
    while count < n:
        b=next(gen)
        count+=1
    return(b)

