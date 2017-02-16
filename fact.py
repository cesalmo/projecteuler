# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:34:31 2017
@author: Cesar Alvarez
"""

def fac(n):
    
   
    
    if n == 1:
        return 1
    
    n=n*fac(n-1)
    
    return n
    