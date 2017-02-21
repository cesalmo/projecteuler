# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:06:40 2017
@author: Cesar Alvarez
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""
b=0
for i in str(2**1000):

    b=b+int(i)
    print('res{}'.format(b))