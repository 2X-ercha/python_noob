from math import *
def print_(x):
    if type(x) == float:
        print("%.4f" % x)
    else:
        print(x)

#第一题
for temp in [-280, -100, 0, 20, 120, 200]:
    #请在下面编写代码
    # ********** Begin ********** #
    if temp<-273.15:
        F='None'
    else:
        F=9/5*temp+32
    # ********** End ********** #
    #请不要修改下面的代码
    print_(F)

print('\n***********************\n')

#第二题
for number in [-101.23, -3.14, 0, 12.55, 1908]:
    # 请在下面编写代码
    # ********** Begin ********** #
    if number<0:
        number=-number
    # ********** End ********** #
    # 请不要修改下面的代码
    print_(number)

print('\n***********************\n')

#第三题
for (num1, num2) in [(12, 34), (-6, -7),(-12, 23), (-273, 0), (0, 199)]:
    # 请在下面编写代码
    # ********** Begin ********** #
    num1,num2=min(num1,num2),max(num1,num2)
    # ********** End ********** #
    # 请不要修改下面的代码
    print(num1, '  ', num2)


print('\n***********************\n')

#第四题

for (num1, num2, num3) in [(-231, -321, 123), (100, 0, -99), (-980, -1002, -1), (6,1,2017)]:
    # 请在下面编写代码
    # ********** Begin ********** #
    num1,num2,num3=min(num1,num2,num3),num1+num2+num3-min(num1,num2,num3)-max(num1,num2,num3),max(num1,num2,num3)
    # ********** End ********** #
    # 请不要修改下面的代码
    print(num1, num2, num3)


print('\n***********************\n')

#第五题

for (num1, num2) in [(10, 5), (12,34), (89,0), (-100, 23), (789, -123)]:
    # 请在下面编写代码
    # ********** Begin ********** #
    if num2==0:
        result='None'
    else:
        result=num1/num2
    # ********** End ********** #
    # 请不要修改下面的代码
    print_(result)


print('\n***********************\n')

#第六题

for (a, b, c) in [(1,2,1), (1,-2,1), (1,2,-3), (12, 34, 56), (78, 89, 100)]:
    # 请在下面编写代码
    # ********** Begin ********** #
    d=b*b-4*a*c
    if d<0:
        root1,root2='None','None'
    else:
        root1=(-b+sqrt(d))/(2*a)
        root2=(-b-sqrt(d))/(2*a)
    # ********** End ********** #
    # 请不要修改下面的代码
    print(root1, root2)


print('\n***********************\n')

#第七题

for x in [-9, -8, -7, -6, -5, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]:
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
    print_(fx)