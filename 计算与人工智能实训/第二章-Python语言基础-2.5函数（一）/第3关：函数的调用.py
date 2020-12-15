#coding=utf-8

#输入数字字符串，并转换为数值列表
a = input()
num1 = eval(a)
numbers = list(num1)
# 请在此添加函数bubbleSort代码，实现编程要求
#********** Begin *********#
def bubbleSort(L):
    L=sorted(L)
    return L
#********** End **********#
print(bubbleSort(numbers))