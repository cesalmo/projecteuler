# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:23:49 2017
@author: Cesar ALvarez
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
#Prime checker
def check_prime(a):
    if a==1 or a==2 or a==3:
        c='YES'
    else:
        for i in range(2,a-1):
            if a%i == 0:
                c = 'NO'
                break
            elif a%i != 0:
                c = 'YES'
                pass
    return(c)

check_prime(11)
#%% Prime generator. 
def prime_gen():
    b = 3
    while True:
        if check_prime(b)=='YES':
            yield(b)
            b+=2
        else:
            b+=2

pr = prime_gen()
#%%
d=600851475143
#d=131950
n=next(pr)
max_prime = 0
while max_prime == 0:
    if d%n == 0:
        max_prime = n
#        print('max prime {}'.format(n))
#        n=next(pr)
    else:
        print('checking {}'.format(n))
        n=next(pr)
    
print('max prime {}'.format(max_prime)) 
