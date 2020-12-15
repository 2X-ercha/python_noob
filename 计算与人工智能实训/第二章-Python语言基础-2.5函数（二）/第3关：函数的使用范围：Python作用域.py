#coding=utf-8

#输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加一个private函数_gcd()求两个正整数的最大公约数
#********** Begin *********#
def _gcd(x,y):
    x,y=max(x,y),min(x,y)
    while y!=0:
        x,y=y,x%y
    return x
#********** End **********#

#请在此添加一个public函数lcm()，在lcm()函数中调用_gcd()函数，求两个正整数的最小公倍数
#********** Begin *********#
def lcm(x,y):
    return int(x*y/_gcd(x,y))
#********** End **********#


#调用函数，并输出a,b的最小公倍数
print(lcm(a,b))