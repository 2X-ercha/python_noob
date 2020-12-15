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