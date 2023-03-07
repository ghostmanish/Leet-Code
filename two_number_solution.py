# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:03:05 2023

@author: mgosh
"""

nums = [3,2,3]

target = 6

k= []

for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if i != j:
            sum1 = nums[i] + nums [j]
            if sum1 == target:
                k.append(i)
                k.append(j)
print(k)