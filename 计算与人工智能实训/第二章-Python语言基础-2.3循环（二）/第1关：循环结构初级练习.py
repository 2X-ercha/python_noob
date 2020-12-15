# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:54:44 2020

@author: hzh
"""
from math import *

i = 1 # 当前计算的值
s = 0 # 计算出来的和
# 第一题
########### begin ##########

# 请在此输入循环控制语句
while i<=999:
######### end     ####
    s = s + i ** 2
    i = i + 2

print(s)

########## 第二题 ##############
x = int(input())

if x<0:
    print('无实数解')
else:
    g = x/2
    #######begin##############
    # 请输入循环控制语句
    while abs(x-g*g)>=0.000001:
    #######end#################
        g = (g+x/g)/2
    print(g)

