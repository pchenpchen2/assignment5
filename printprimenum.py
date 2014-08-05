# -*- coding: utf-8 -*-
"""
Created on Mon Aug 04 11:44:36 2014

@author: pchen
"""

for i in range (2,1001):    
    prime_num = True;
    for j in range(2,i):       
        if (i%j == 0):
            prime_num = False;            
            break
    if (prime_num == True):
        print i,
    
        