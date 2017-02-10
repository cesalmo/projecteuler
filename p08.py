# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:07:30 2017
@author: Cesar Alvarez
The four adjacent digits in the 1000-digit number that have the greatest 
    product are 9 × 9 × 8 × 9 = 5832
Find the thirteen adjacent digits in the 1000-digit number that have the 
    greatest product. What is the value of this product?
"""

def string_product(n,digit_number):

    data = {}
        
    #brute force##########
    #for i in range(0,len(n)-13):
    ##    print('pos={}'.format(i))
    #    a=str(n)[i:i+13]
    #    mul=1
    #    
    #    for b in a:
    #        mul=mul*int(b)
    #    data[mul]=a
    
    
    for i in range(0,len(n)-digit_number): #iterate number
    #    print('pos={}'.format(i))
        a=str(n)[i:i+digit_number] #get string
        _sum=0 #var init
        for b in a:
    #        print(b)
            _sum=_sum+int(b) #string sum
        aver=_sum/digit_number #average
        t1=0
        for b in a:
            t1=t1+(int(b)-aver)**2
        std=(t1/digit_number)**0.5 #std dev
        floor=aver**4-2*aver**2*std**2+std**4 #floor function
        ceil=aver**4 #ceil function
    
        
        data[i]=(floor,ceil,a) #populate dict
    
    data_new={}  #delete rows with '0'
    for i,(floor,ceil,a) in data.items(): 
        if a.find('0') == -1:
            data_new[i]=(floor,ceil,a)
             
           
    data_floor=sorted(data_new.items(), key=lambda e:e[1][0], reverse=True) #sorted by floor
    data_ceil=sorted(data_new.items(), key=lambda e:e[1][1], reverse=True) #sorted by ceiling
    
    filtered_list=[] #filtered by: ceiling >= floor
    for i in range(0,len(data_ceil)):
        if data_ceil[i][1][1] >= data_floor[0][1][0]:
            filtered_list.append(data_ceil[i])
    
    final_data={}
    for i in range(0,len(filtered_list)): #get products
    #    print('pos={}'.format(i))
        a=filtered_list[i][1][2]
        mul=1
        
        for b in a:
            mul=mul*int(b)
        
        final_data[mul]=a  
    
    final_data_sorted=sorted(final_data.items(), reverse=True) 
    
    return(final_data_sorted[0])
    
if __name__=='__main__':
    
    n='''
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450'''.replace('\n','')
    n=n.replace(' ','')
    
    print(string_product(n,13)) #(product,'string')