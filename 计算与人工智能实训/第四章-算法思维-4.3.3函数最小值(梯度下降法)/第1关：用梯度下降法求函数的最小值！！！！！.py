# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:52:37 2020

@author: hyr
"""

cur_x = 10  # 当前 x 值，通过参数可以提供初始值
learning_rate = 0.2  # 学习率，也相当于设置的步长
precision = 0.000001  # 设置收敛精度
max_iters = 10000  # 最大迭代次数


def f(x):
    return x ** 2 - 54 / x


def df(x):
    return 2 * x + 54 * x ** (-2)


def gradient_descent_1d(cur_x=0.1, learning_rate=0.01, precision=0.0001, max_iters=10000):
    for i in range(max_iters):
        grad_cur = df(cur_x)
        if abs(grad_cur) < precision:
            break  # 当梯度趋近为 0 时，视为收敛
        cur_x = cur_x - grad_cur * learning_rate
    return cur_x

##########begin###########


############end#############
minValue_x = gradient_descent_1d(cur_x=-10, learning_rate=0.2, precision=0.000001, max_iters=10000)
minValue = f(minValue_x)
print("%.7f" % minValue_x)

#-3.0000001