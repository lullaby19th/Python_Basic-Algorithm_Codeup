# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:03:48 2019

@author: 노민준
"""


a, b = input().split('-') # -을 기준으로 분리하여 변수에 차례대로 저장

x = int(a)
y = int(b)

print('%06d%d' %(x,y)) # 이렇게 표현해야 공백이 생기지 않는다.

# %06d 총6칸을 사용해서 표현하는데 나머지는 0으로 표현한다.