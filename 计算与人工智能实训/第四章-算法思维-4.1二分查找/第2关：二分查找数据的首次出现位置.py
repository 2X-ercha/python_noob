# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 07:44:05 2020

@author: hyr
"""


def binary_search_2(A, x):
    ##########begin##########
    a, b = 0, len(A) - 1
    while (a < b):
        mid = (a + b) // 2
        if A[a] <= x <= A[mid]:
            b = mid
        else:
            a = mid + 1
    if a > b:
        return -1
    else:
        return a
    ############end###########


A = [1, 3, 6, 6, 8, 8, 16, 16, 16, 27, 29, 35]
num = 16

index = binary_search_2(A, num)
if index != -1:
    print('数%d在数组' % (num), A, '中首次出现的下标为%d' % (index))


