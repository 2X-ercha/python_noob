'''

本关任务：天天向上的力量。

相关知识（略）
编程要求
根据提示，在右侧编辑器补充代码，计算并输出结果。
   一年365天，以第1天的能力值为基数，记为1.0，当好好学习时能力值相比前一天提高1‰，当没有学习时由于遗忘等原因能力值相比前一天下降1‰。每天努力和每天
   放任，一年下来的能力值相差多少呢？
import math
dayup = math.pow((1.0 + 0.001), 365) # 每天提高0.001
daydown = math.pow((1.0 - 0.001), 365) # 每天荒废0.001
print(“向上: %.2f, 向下: %.2f.”%(dayup, daydown))
如果按5‰提高与下降对比一年的能力值相差多少呢？
import math
dayup = math.pow((1.0 + 0.005), 365) # 每天提高0.005
daydown = math.pow((1.0 - 0.005), 365) # 每天荒废0.005
print(“向上: %.2f, 向下: %.2f.”%(dayup, daydown))

任务一：俗语“三天打鱼两天晒网”，一年下来能力值又会是多少呢？请补全代码完成程序编写

任务二：如果按工作日5天学习，周末2天休息每天相比前一天下降1%，工作日要努力到什么程度，一年后的水平才能与每天努力1%取得的效果一样呢？请补全代码完成程
序编写。

任务三：尽管每天坚持，但人的能力发展并不是无限的，它符合特定模型，假设能力增长符合以下模型：以7天为一周期，连续学习3天能力值不变，但从第4天开始至第7天
每天能力增长为前一天的1%，如果7天中有一天间断学习，则周期从头计算，请编写程序，如果初始能力为1，固定每10天休息一天， 365天后能力值是多少，请补全代码
完成程序编写。

'''

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:49:56 2020

@author: hzh
"""
from math import *

# 任务一：三天打鱼两天晒网
dayup, dayfactor = 1.0, 0.01
# 请在下面编写代码
# ********** begin ********** #
up,down=3,2
dayup = pow(((dayup+dayfactor)**3*(dayup-dayfactor)**2),365/5)
# ********** End ********** #
# 请不要修改下面的代码
print("{:.2f}.".format(dayup))

# 任务二：天天向上的力量
#import math

import numpy as np
dayup, dayfactor = 1.0, 0.01
ddup = pow((dayup + dayfactor), 365)
# print("天天向上的力量: {:.2f}.".format(ddup))
# 请在下面编写代码
# ********** Begin ********** #
for i in np.arange(0.01,1.,0.001):
    if pow(((dayup+i)**5*(dayup-dayfactor)**2),365//7)*(dayup+i)>=ddup:
        dayfactor=i
        break
# ********** End ********** #
# 请不要修改下面的代码
print("{:.4f}.".format(dayfactor))

# 任务三：天天向上续
#from math import *

Restday = 10  # 休息10天,
dayup, dayfactor = 1.0, 0.01  # 初始值
# 请在下面编写代码
# ********** Begin ********** #
dayup=pow((dayup+dayfactor)**4,365//10)*(dayup+dayfactor)**2
# ********** End ********** #
# 请不要修改下面的代码

print("{:.2f}".format(dayup))  #

'''
2.04.
0.0190.
4.27
'''