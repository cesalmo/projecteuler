# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:27:19 2017

@author: cesar
"""
import itertools
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

if __name__ == '__main__':
        
    aa=eratosthenes()
    d=600851475143
    #d=131950
    n=next(aa)
    max_prime = 0
    while n < 131951:
        if d%n == 0:
            max_prime = n
            print('max prime {}'.format(n))
            n=next(aa)
        else:
            print('checking {}'.format(n))
            n=next(aa)
        
    print('max prime {}'.format(max_prime)) 
