# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:02:52 2017
@author: Cesar Alvarez
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less 
than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.

"""
import time
starttime = time.time()
for b in range(10,100):
    for a in range(10,b):
#        print(a,b)
#%%
        
#        a=49
#        b=99

        a=str(a)
        b=str(b)
        
        if a[1]=='0' and b[1]=='0':
            pass
        else:
            for c in range(0,len(a)):
                if b.count(a[c]) == 0:
                    pass
                elif b.count(a[c]) == 1:
                    if a.count(a[c])==2:
                        if int(b.replace(a[c],''))==((int(b)*int(a[0]))/(int(a))):
                            print(a,b)
                            print(a[0], b.replace(a[c],''))
                    else:
                        if int(b.replace(a[c],'')) == (int(b)*int(a.replace(a[c],''))/(int(a))):
                            print(a,b)
                            print(a.replace(a[c],''), b.replace(a[c],''))
                elif b.count(a[c]) == 2:
                    if int(b[0]) == (int(b)*int(a.replace(a[c],''))/(int(a))):
                        print(a,b)
                        print(a.replace(a[c],''), b[0])
print('time={}'.format(time.time() - starttime))