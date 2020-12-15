import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt  # 导入matplotlib.pyplot
import matplotlib.image as imgplt


# 第一题：求三角形阴影部分面积
# 请编写函数triArea(a ,b , c)，返回三角形的面积
def triArea(a, b, c):
    # 请在下面编写代码
    ######## begin ###########
    p = (a + b + c) / 2
    Area = np.sqrt(p * (p - a) * (p - b) * (p - c))
    ######## end #############
    # 请不要修改下面的代码
    return Area


S1 = triArea(9.8, 9.3, 6.4)
S2 = triArea(2.9, 4.1, 4.7)
S3 = triArea(2.0, 1.4, 2.3)
print('%.6f' % (S1 - S2 + S3))
print('\n***********************\n')


# 第二题：哥德巴赫猜想
# 请编写函数isPrime(x)。判断x是否为素数，如果是素数则返回True否则返回False
def isPrime(n):
    # 请在下面编写代码
    ######## begin ###########
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#######  end ############

def Goldbach(N):  # 将N分解成两素数之和
    if N < 6 or N % 2 == 1:  # 若N小于6或N为奇数
        print('N应该是大于等于6的偶数')
    else:
        # 循环判断，得到符合要求的小于N的两个素数，并打印
        for x in range(2, N // 2 + 1):  # 想想为什么是从2到N/2
            # 调用isPrime函数得到符合要求的小于N的两个素数
            ######## begin ###########
            if isPrime(x) and isPrime(N - x):
                ######## end ###########
                print(N, '=', x, '+', N - x)
                break


for num in [88, 68, 50, 1000]:
    Goldbach(num)
print('\n***********************\n')


# 第三题 ：信用卡的验证程序
def validCreditCard(num):
    # 请在下面编写代码
    # ********** Begin ********** #
    strnum=str(num)
    if len(strnum)!=8:
        return False
    a=int(strnum[-1])+int(strnum[-3])+int(strnum[-5])+int(strnum[-7])
    u1=str(int(strnum[-2])*2)
    u2=str(int(strnum[-4])*2)
    u3=str(int(strnum[-6])*2)
    u4=str(int(strnum[-8])*2)
    u,b=u1+u2+u3+u4,0
    for i in range(0,len(u)):
        b+=int(u[i])
    if (a+b)%10==0:
        valid=True
    else:
        valid=False
    # ********** End ********** #
    # 请不要修改下面的代码
    return valid


for num in [1234567, 43589795, 87539319, 123456789]:
    valid = validCreditCard(num)
    print(valid)
print('\n***********************\n')

'''
a) 对给定的8位信用卡号码，如43589795，从最右边数字开始，隔一位取一个数相加，如5+7+8+3=23。
b) 将卡号中未出现在第一步中的每个数字乘2，然后将相乘的结果的每位数字相加。例如，对上述例子，未出现在第一步中的数字乘2后分别为（从右至左）18、18、10、8，则将所有数字相加为1+8+1+8+1+0+8=27。
c) 将上述两步得到的数字相加，如果得数个位为0，则输入的信用卡号是有效的。
'''


# 第四题：打印日历程序
def day(y, m, d):  # 计算y年m月d日是星期几
    # 请在下面编写代码
    # ********** Begin ********** #
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    # ********** End ********** #
    # 请不要修改下面的代码
    return d0


def isLeapYear(year):  # 判断year年是否闰年
    # 请在下面编写代码
    # ********** Begin ********** #
    if (year%100!=0 and year%4==0) or year%400==0:
        return True
    # ********** End ********** #
    # 请不要修改下面的代码
    return False


def calendar(y, m):  # 打印y年m月日历
    print('       {}年{}月'.format(y, m))
    print('Su\tM\tTu\tW\tTh\tF\tSa')
    # 请在下面编写代码
    # ********** Begin ********** #
    t=day(y,m,1)%7
    print('\t'*t,end='')
    for i in range(1,7-t+1):
        print('{}\t'.format(i),end='')
    x=7-t+1
    print('')
    big=[1,3,5,7,8,10,12]
    if m in big:
        maxday=31
    elif m==2:
        if isLeapYear(y):
            maxday=29
        else:
            maxday=28
    else:
        maxday=30
    while x<=maxday:
        for i in range(1,8):
            if x>maxday:
                break
            print('{}\t'.format(x), end='')
            x+=1
        print('')
    # ********** End ********** #
    # 请不要修改下面的代码

'''
def calendar(y, m):  # 打印y年m月日历
    print('       {}年{}月'.format(y, m))
    print('Su\tM\tTu\tW\tTh\tF\tSa')
    # 请在下面编写代码调用函数计算y年m月1日是星期几保存在变量date中
    # ********** Begin ********** #
    date = day(y, m, 1)
    # ********** End ********** #
    days = 0
    # 请在下面编写代码计算y年m月的天数
    # ********** Begin ********** #
    big = [1, 3, 5, 7, 8, 10, 12]
    if m in big:
        days = 31
    elif m == 2:
        if isLeapYear(y):
            days = 29
        else:
            days = 28
    else:
        days = 30
    # ********** End ********** #
    count = date  # y年m月1日是星期几
    for i in range(date):
        print('\t', end='')
    for d in range(1, days + 1):
        print(str(d) + '\t', end="")
        count = (count + 1) % 7
        if count == 0:
            print()
    print()
'''

for (y, m) in [(2017, 8), (2017, 10), (2015, 8), (2017, 2), (2016, 2)]:
    calendar(y, m)
    print('---------------------------')

print('\n***********************\n')
