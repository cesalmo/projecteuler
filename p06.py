# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:42:22 2017
@author: Cesar Alvarez
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

b=0
for x in range(1,101):
    a=x**2
    b=b+a
    print('calc. {}'.format(x))

n=0
for i in range(1,101):
    n=n+i

o=n**2

print(o-b)
