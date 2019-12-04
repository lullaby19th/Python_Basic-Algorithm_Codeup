# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:03:04 2019

@author: 노민준
"""

a, b, c = input().split('.') # .을 기준으로 분리하여 변수에 차례대로 저장

x = int(a)
y = int(b)
z = int(c)
print('%04d.%02d.%02d' %(x,y,z))

# %02d를 사용하면 2칸을 사용해 출력하는데, 
# 한 자리 수인 경우 앞에 0을 붙여 출력한다.

# print('%d,%d' %(a,b)) 이런식으로 표현해야 공백이 생기지 않는다.
