# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:37:47 2019

@author: 노민준
"""
#%%
a = input()

for i in range(len(a)):
    b = str(10**(len(a)-1-i))
    c = a[i] + b[1:]
    print('[%s]' %c)
#%%
n=input()

print("["+str(int(n[0])*10000)+"]")
print("["+str(int(n[1])*1000)+"]")
print("["+str(int(n[2])*100)+"]")
print("["+str(int(n[3])*10)+"]")
print("["+str(int(n[4]))+"]")
