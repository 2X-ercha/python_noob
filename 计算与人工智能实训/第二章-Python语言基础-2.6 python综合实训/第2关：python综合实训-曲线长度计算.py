# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:23:58 2020

@author: hzh
"""
import numpy as np
import matplotlib.pyplot as plt


# 在此添加代码，定义函数f(x)，计算f(x)的值
########### begin #############
def f(x):
    return np.exp(x)*np.sin(x)
########### end #############

# 在此添加代码，编写函数pt(a, b)，利用勾股定理计算直角三角形的斜边长
########### begin #############
def pt(a,b):
    ya,yb=f(a),f(b)
    return np.sqrt((b-a)**2+(ya-yb)**2)
########### end #############

def cav_len(n):  # 曲线细分成n个子区间
    x = np.linspace(0, np.pi, n + 1)  # n个子区间的n+1个端点
    len, h = 0, np.pi / n  # len为曲线长度、h为子区间宽度
    # 在此添加代码，通过循环调用函数pt()，f(x)计算曲线的长度
    ########### begin #############
    for i in x[:-1]:
        len+=pt(i,i+h)
    ########### end #############
    return len


n = 1000  # 细分成n个子区间
print('len = %.6f' % cav_len(n))  # 函数调用输出结果