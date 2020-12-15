#coding=utf-8

#输入一个整数n
n =  int(input())

# 请在此添加代码，实现编程要求
#********** Begin *********#
def prime(n):
    if n==1:
        return 'False'
    if n==2:
        return 'True'
    for i in range(2,n):
        if n%i==0:
            return 'False'
    return 'True'
#********** End **********#
print(prime(n))