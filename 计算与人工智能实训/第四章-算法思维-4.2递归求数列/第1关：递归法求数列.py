# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 08:15:07 2020

@author: hyr
"""


def f(n):
    ######begin#######
    if n == 0: return 3
    if n == 1: return 26
    return f(n - 1) + f(n - 2)

    ######end##########


num = eval(input())
print(f(num))

