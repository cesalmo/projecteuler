# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:24:33 2017
@author: Cesar Alvarez
"""

mil = 10

tb = dict()
ans = 0
maxn = -1
tb[1] = 1

def solve(n):
    if n not in tb:
        print('n={}'.format(n))
        print(n // 2 if n % 2 == 0 else 3 * n +1 )
        tb[n] = solve(n // 2 if n % 2 == 0 else 3 * n + 1)+1
        print('tb[]={}'.format(tb[n]))
    return tb[n]
#%%
for n in range(1, mil):
    cnt = solve(n)
    if maxn < cnt:
        maxn = cnt
        ans = n


print(ans)
