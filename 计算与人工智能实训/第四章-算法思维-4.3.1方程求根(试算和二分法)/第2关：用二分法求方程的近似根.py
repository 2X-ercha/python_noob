# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:06:16 2020

@author: hyr
"""

import numpy as np
def f(x):
    return x**3-x-1
a=-10;b=10 #a,b为根所在的左右边界，n记录迭代次数
err=0.000001
while a<=b:
    ########begin#######
    mid=(a+b)/2
    if abs(f(mid))<=err:
        break
    if f(a)*f(mid)<=0:b=mid
    else:a=mid
    #########end#########
x=mid
print(x)


