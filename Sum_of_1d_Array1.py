# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:33:00 2023

@author: mgosh
"""
nums = [3,1,2,10,1]

for i in range(1,len(nums)):
    nums[i]+=nums[i-1]
print(nums)