# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:02:38 2020

@author: hyr
"""

import numpy as np
def f(x):
    return x**3-x-1
x=1;h=1;err=0.000001 #根的初始值设为1，初始步长h为1
while(np.abs(f(x))>=err):
    ############begin#########
    if f(x)<0:x+=h
    else:x-=h
    h/=2
    ##############end##########
print(x)