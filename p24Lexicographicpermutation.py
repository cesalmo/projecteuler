# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:04:38 2017
@author: Cesar Alvarez
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time
starttime = time.time()

def perm(intlist):
    '''permutations of a list of elements
    '''
#case: [a,b]    
    if len(intlist) == 2 and isinstance(intlist[0],int):
        return([[intlist[0],intlist[1]],[intlist[1],intlist[0]]])
#case: [a,b,c...]
    if isinstance(intlist[0],int):
#slice [a,b,c,d..] untill [a,b] 
        listperm=list()      
        for i in perm(intlist[1:]):
#case: [[a,b,c...],[a,b,c...],...]
#i=[1,2] j=len(i)--> insert intlist[0] at position j
            for j in range(0,len(i)+1):
                listperm.append(i[0:j]+[intlist[0]]+i[j:])
        return(listperm)
                
if __name__=='__main__':
    
    print(sorted(perm([0,1,2,3,4,5,6,7,8,9]))[999999])
    print(time.time() - starttime)