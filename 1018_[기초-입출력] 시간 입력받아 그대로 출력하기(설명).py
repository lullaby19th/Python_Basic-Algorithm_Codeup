# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 00:35:54 2019

@author: 노민준
"""

a, b = input().split(':') # :을 기준으로 분리하여 변수에 차례대로 저장

x = int(a)
y = int(b)

print('%d:%d' %(x,y))

# print(x,':',y)는 3 : 16 으로 공백이 포함되서 나옴 
