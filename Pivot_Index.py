# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:42:51 2023

@author: mgosh
"""

nums = [1,7,3,6,5,6]
count = -5
leftSum, rightSum = 0, sum(nums)
for idx, ele in enumerate(nums):
    rightSum -= ele
    if rightSum == leftSum:
        count = idx
    leftSum += ele
if count>0:
    print(count)
    
else:
    if count == 0:
        print(0)
    else:
        print(-1)