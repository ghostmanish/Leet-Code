# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:15:45 2023

@author: mgosh
"""

nums = [3,1,2,10,1]

k = []

for i in range(0,len(nums)):
    if i == 0:
        k.append(nums[i])
    else:
        k.append(k[i-1] + nums[i])
print(k)