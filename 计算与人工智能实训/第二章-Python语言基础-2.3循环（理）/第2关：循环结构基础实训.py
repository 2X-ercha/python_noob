# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:25:23 2020

@author: hzh
"""
from random import *
import numpy as np

# 第一题
# 请在下面编写代码
# ********** Begin ********** #
print('摄氏温度\t\t华氏温度')
print('********************')
for i in range(-40, 51, 5):
    # ********** End ********** #
    # 请不要修改下面的代码
    f = 1.8 * i + 32
    print('{}\t\t{:.1f}'.format(i, f))
print('\n***********************\n')

# 第二题

numbers = []
i = 0
# 请在下面编写代码
# ********** Begin ********** #
while i <= 300:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        numbers.append(i)
    i += 1
# ********** End ********** #
# 请不要修改下面的代码
print(numbers)

print('\n***********************\n')

# 第三题：输出100以内的素数。

numbers = []  # 存放结果的列表

# 请在下面编写代码
# ********** Begin ********** #
for i in range(2, 100):
    temp = 0
    for j in range(2, int(np.sqrt(i)) + 1):
        if i % j == 0:
            temp = 1
    if not temp:
        numbers.append(i)
# ********** End ********** #
# 请不要修改下面的代码
print(numbers)

print('\n***********************\n')

# 第四题求：1-3！+5!-7！......(-1)n-1(2n-1)!,求前n的项的和
number = [2, 4, 5, 7, 10]  # n取值来自列表
result = []  # 存放结果的程序

for n in number:
    # 请在下面编写代码
    # ********** Begin ********** #
    ans = 0
    for i in range(1, n + 1):
        nowans = 1
        t = 2 * i - 1
        for j in range(1, t + 1):
            nowans *= j
        ans += -(-1) ** i * nowans
    result.append(ans)
# ********** End ********** #
# 请不要修改下面的代码
print(result)

print('\n***********************\n')

# 第五题 ：求sin(x)的值
from math import *

Number = [pi, pi / 2, pi / 4]  # x的取值
result = []

#阶层运算函数
def jc(x):
    ans=1
    for i in range(1,x+1):
        ans*=i
    return ans

for x in Number:
# 请在下面编写代码
# ********** Begin ********** #
    i,res,t=1,x,1
    while abs(t)>=0.0000001:
        u=2*i+1
        t=(-1)**i*x**u/jc(u)
        res+=t
        i+=1
    res-=t #最后一项不加
    result.append(res)
# ********** End ********** #
for num in result:
    print("output=%.10f" % num)
# 请不要修改下面的代码
print('\n***********************\n')

# 第六题 #求数列队中两个数的最大公约数

Number = [(8, 6), (12, 18), (15, 8), (100, 75)]
greatcd = []  # 保存最大公约数
for a, b in Number:
# 请在下面编写代码
# ********** Begin ********** #
    while b!=0:
        a,b=b,a%b
    greatcd.append(a)
# ********** End ********** #
# 请不要修改下面的代码
print(greatcd)

print('\n***********************\n')