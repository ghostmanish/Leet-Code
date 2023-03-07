# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:28:32 2023

@author: mgosh
"""

s = "lleettcdde"
count = 0
for i in range(0, len(s)):
    if s.count(s[i]) == 1:
        count = s[i]
        break
if count:
    print(s.index(count))
else:
    print(-1)