# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:20:46 2017
@author: Cesar Alvarez
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
import time

i,j=20,20 #insert rows and columns

mem={(i,0):1 for i in range(1,i+1)}
mem.update({(0,j):1 for j in range(1,j+1)})


def path(i,j):

    
    if mem.get((i,j)) == None:
#        print('in i{},j{}'.format(i,j))
#        print('(i{},j{})+(i{},j{})'.format(i-1,j,i,j-1))
        mem[i,j]=path(i-1,j)+path(i,j-1)
#        print('out i{},j{}={}paths'.format(i,j,mem[i,j]))
    
        
    return(mem[i,j])

if __name__=='__main__':
    
    start = time.time()
    result=path(i,j)
    elapsed = time.time() - start
 
    print("result {} found in {} seconds".format(result, elapsed))