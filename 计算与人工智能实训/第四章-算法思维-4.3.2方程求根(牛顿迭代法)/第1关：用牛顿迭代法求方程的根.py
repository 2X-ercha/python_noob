# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:09:13 2020

@author: hyr
xex-1=0  初值x0=0.5
"""

import numpy as np
def f(x):
    return x*np.exp(x)-1
def df(x):
    ########begin######
    return (x+1)*np.exp(x)
    #########end#########
x=0.5;fx=f(x);dfVal=df(x)
err=0.000001;n=0
while(np.abs(fx)>=err):
    #########begin##########
    x=x-fx/dfVal
    fx=f(x)
    dfVal=df(x)
    ##########end##########
print("%.8f" % x)
