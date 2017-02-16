# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:20:46 2017
@author: Cesar Alvarez
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

import time
 
 
gridSize = [2,3]
 
def recPath(gridSize):
    """
    Recursive solution to grid problem. Input is a list of x,y moves remaining.
    """
    # base case, no moves left
    if gridSize == [0,0]: return 1
    # recursive calls
    paths = 0
    # move left when possible
    if gridSize[0] > 0:
        print('pre-path x{}'.format(paths))
        print('pregrid{}'.format(gridSize[0]-1))
        paths += recPath([gridSize[0]-1,gridSize[1]])
        print('post-path x{}'.format(paths))
        print('postgrid{}'.format(gridSize[0]-1))
    # move down when possible
    if gridSize[1] > 0:
#        print('pre-path y{}'.format(paths))
        paths += recPath([gridSize[0],gridSize[1]-1])
#        print('post-path y{}'.format(paths))
 
    return paths
 
start = time.time()
result = recPath(gridSize)
elapsed = time.time() - start
 
print("result {} found in {} seconds".format(result, elapsed))