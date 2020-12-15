# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:27:35 2020

@author: hzh
"""
#第一题
for (Weight,Height) in [(60,1.65),(40,1.60),(80, 1.70),(75,1.83),(88,1.80)]:
    #请在下面编写代码
    #wto, dom的结果为字符串类型的"肥胖"，"偏瘦"，"偏胖"，"正常"
    # ********** Begin ********** #
    BMI=Weight/(Height*Height)
    if BMI<18.5:
        wto,dom='偏瘦','偏瘦'
    elif BMI>=18.5 and BMI<24:
        wto,dom='正常','正常'
    elif BMI>=24 and BMI<25:
        wto,dom='正常','偏胖'
    elif BMI>=25 and BMI<28:
        wto,dom='偏胖','偏胖'
    elif BMI>=28 and BMI<30:
        wto,dom='偏胖','肥胖'
    else:
        wto,dom='肥胖','肥胖'
    # ********** End ********** #
    #请不要修改下面的代码
    print("BMI 指标为:国际'{0}', 国内'{1}'".format(wto, dom))
print('\n******************************\n')

#第二题
for salary in [-1000, 0, 40000, 47450, 98000, 114650, 14980, 17470, 25670, 311950, 360000]:
    # 请在下面编写代码
    # ********** Begin ********** #
    salaTax=salary
    if salary<=0:
        salaTax=0
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
    print("%.4f" %salaTax)
print('\n***********************\n')

#第三题
for (p1, p2) in [('s', 'j'), ('b', 'j'),('j', 'j'), ('b', 's')]:
    # 请在下面编写代码
#p1,p2代表玩家1，玩家2，'s','j','b' 分别代表石头剪刀和布
#game=-1，0，1分别代表p1输局，平局，赢局
    # ********** Begin ********** #
    if p1==p2:
        game=0
    elif p1=='j' and p2=='b' or p1=='s' and p2=='j' or p1=='b' and p2=='s':
        game=1
    else:
        game=-1
    # ********** End ********** #
    # 请不要修改下面的代码
    print(game)
print('\n***********************\n')
