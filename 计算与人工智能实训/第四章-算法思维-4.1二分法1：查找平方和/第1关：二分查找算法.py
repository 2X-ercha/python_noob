# 二分查找
def binary_search(A, x):
########## begin ##########
# 请在此填写代码，找到x返回索引号，没找到返回-1
    left,right=0,9999
    while left<right:
        median=(left+right)//2
        if A[left]<=x<=A[median]:
            right=median
        else:
            left=median+1
    if A[left]==x:
        return left
    else:
        return -1
########## end ##########

import random

random.seed(177)  # 随机数种子，使得A里面的数固定
# 在1到百万的范围内，生成1万个数字
A = [random.randint(1, 1000000) for i in range(10000)]
A.sort()
x = int(input())
index = binary_search(A, x)
print(index)