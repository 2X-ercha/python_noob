# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:48:47 2020

@author: hzh
"""
from random import *
from math import *

r = []
for i in [10, 200,300,400,500,600,700,800,900,1000]:
    seed(i)
    r.append(randint(1, i))

def print_(x):
    if type(x) == float:
        print("%.4f" % x)
    else:
        print(x)


#第一题

def sumInt(n):
    #请在下面编写代码
    # ********** Begin ********** #
    if n<0:
        return 'None'
    if n==0 or n==1:
        return n
    summary=sum(range(1,n+1))
    # ********** End ********** #
    #请不要修改下面的代码
    return summary


#第二题

def factorial(n):
    #请在下面编写代码
    # ********** Begin ********** #
    if n<0:
        return 'None'
    if n==0 or n==1:
        return 1
    fac=1
    for i in range(2,n+1):
        fac*=i
    # ********** End ********** #
    #请不要修改下面的代码
    return fac

#第三题

def isPrime(n):
    # 请在下面编写代码
    # ********** Begin ********** #
    if n==1:
        return 'False'
    if n==2:
        return 'True'
    for i in range(2,n):
        if n%i==0:
            return 'False'
    return 'True'
    # ********** End ********** #
    # 请不要修改下面的代码
    return (isprime)

#第四题

def f(x):
    # 请在下面编写代码
    # ********** Begin ********** #
    if x>=-10 and x<-8:
        fx=x-2
    elif x>=-8 and x<-6:
        fx=x+3
    elif x>=-6 and x<=-2:
        fx=x*x
    elif x>-2 and x<2:
        fx=abs(x)
    elif x>=2 and x<=4:
        fx=x**3
    elif x>4 and x<=6:
        fx=3*x-4
    elif x>6 and x<=8:
        fx=4*x+1
    # ********** End ********** #
    # 请不要修改下面的代码
    return fx


#第五题

def tax(salary):
    #请在下面编写代码
    # ********** Begin ********** #
    salaTax=salary
    if salary==0:
        salaTax=0.
    elif salary<0:
        salaTax='None'
    elif salary>0 and salary<=47449:
        salaTax*=0.22
    elif salary>=47450 and salary<=114649:
        salaTax*=0.25
    elif salary>=114650 and salary<=174699:
        salaTax*=0.28
    elif salary>=174700 and salary<=311949:
        salaTax*=0.33
    else:
        salaTax*=0.35
    # ********** End ********** #
    # 请不要修改下面的代码
    return salaTax

if __name__ == '__main__':
    for num in [-10, 0, 10, 100, 1000, 10000]:
        summary = sumInt(num)
        print(summary)
    print('\n***********************\n')

    for num in [-5, 0, 10, 15, 20, 25, 30]:
        fac = factorial(num)
        print(fac)
    print('\n***********************\n')

    for num in r:
        isprime = isPrime(num)
        print(isprime)
    print('\n***********************\n')

    for x in [-9, -8, -7, -6, -5, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]:
        fx = f(x)
        print(fx)

    print('\n***********************\n')
    for salary in [-1000, 0, 40000, 47450, 98000, 114650, 14980, 17470, 25670, 311950, 360000]:
        st = tax(salary)
        print_(st)

