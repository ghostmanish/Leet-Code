# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:46:58 2023

@author: mgosh
"""

l1 = [2,4,3]

l2 = [5,6,4]

k = []
temp = 0
for i in range(0,len(l1)):
    sum1 = l1[i] + l2[i] + temp
    if sum1//10 > 0:
        k.append(sum1%10)
        temp = sum1//10
    else:
        k.append(sum1)
print(k)