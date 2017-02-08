# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:56:14 2017
@author: cesar
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
#○import pdb

def check_pal(a):
    ori=str(a)
    end=ori[::-1]
    
    if end == ori:
        return(True)
    else:
        return(False)

def gen_pal(start, stop):
    plist=[]
    for i in range(start,stop):
        if check_pal(i) == True:
            plist.append(i)
        else:
            pass
    return(plist)  


def search_factor(min_thr,max_thr,pal):
    '''search factor for palindrome:
        data= min and max threeshold for factor search and palindrome
        return true when found
    '''
    #get factor.
    if max_thr - int(pal**0.5) < int(pal**0.5) - min_thr: #99,10=max_val,min_val
        i=int(pal**0.5)
        while i <= max_thr: #99=max_val
            print('checking {} from {}'.format(i,pal))
            i +=1
            if pal%i == 0:
                print('found factor {} for palindrome {}'.format(i,pal))
                return(True)
                break
    
    else:
    #    pdb.set_trace()
        i=int(pal**0.5)
        while i >= min_thr: #10=min_val
            print('checking {} from {}'.format(i,pal))
            if pal%i == 0:
                print('found factor {} for palindrome {}'.format(i,pal))
                return(True)
                break
            i-=1
    

if __name__ == '__main__':
    plist=gen_pal(100*100,999*999)
    plist.reverse()
    for i in plist:
        res=search_factor(100,999,i)
        if res==True:
            break

   
