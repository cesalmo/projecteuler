# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:34:31 2017
@author: Cesar Alvarez
"""
@memoize
def fac(number):
    ''' factorial of a non-negative integer
    '''
    if number == 1:
        return 1
    number = number*fac(number-1)
    return number
