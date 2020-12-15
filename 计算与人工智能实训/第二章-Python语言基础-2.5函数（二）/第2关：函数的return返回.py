#coding=utf-8

#输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加函数gcd代码，求两个正整数的最大公约数
#********** Begin *********#
def gcd(x,y):
    x,y=max(x,y),min(x,y)
    while y!=0:
        x,y=y,x%y
    return x
#********** End **********#

#调用函数，并输出最大公约数
print(gcd(a,b))


def gcd1(x,y):
    x,y=max(x,y),min(x,y)
    while y!=0:
        x,y=y,x%y
    print(x)

a=gcd1(a,b)