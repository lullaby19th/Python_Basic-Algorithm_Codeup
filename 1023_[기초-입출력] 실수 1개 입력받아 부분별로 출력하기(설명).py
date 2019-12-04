# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:26:28 2019

@author: 노민준
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 01:17:25 2019

@author: 노민준
"""
#%%
a = input()

b = int(a[0:a.index('.')])
c = int(a[a.index('.')+1:])

print('%d\n%d' %(b,c))
#%%
a,b=input().split('.')

print(int(a))
print(int(b))
