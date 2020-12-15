# -*- coding: utf-8 -*-

import random, math


# 二分查找
def binary_search(A, x, i):
    ########## begin ##########
    # 请在此填写代码，找到x返回索引号，没找到返回-1
    left, right = i, 9999
    while left < right:
        median = (left + right) // 2
        b = math.sqrt(x - a ** 2)
        if A[left] <= b <= A[median]:
            right = median
        else:
            left = median + 1
    if a ** 2 + A[left] ** 2 == x:
        print(a, A[left])
        return True
    ########## end ##########

random.seed(17)  # 随机数种子，使得A里面的数固定
# 在1到1千的范围内，生成1万个数字
A = [random.randint(1, 1000) for i in range(10000)]
A.sort()  # 排序
X = int(input())
founded = False
for i, a in enumerate(A[:-1]):  # 遍历前n-1个数
    ########## begin ##########
    # 请在此填写代码，输出找到的a和b，没找到返回-1
    founded = binary_search(A, X, i)
    if founded: break
########## end ##########
if not founded: print('-1')