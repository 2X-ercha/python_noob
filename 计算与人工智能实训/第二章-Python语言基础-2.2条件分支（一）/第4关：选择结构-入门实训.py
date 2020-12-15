# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:49:20 2020

@author: hzh
"""
# 第一题

month = int(input())
# 31天的月份：1~7之间的奇数月、8~12之间的偶数月
# 如果是31天的月份输出yes
####### begin #######
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print('yes')
####### end #########
# 如果不是31天的月份，输出no
####### begin #######
else:
    print('no')
####### end #########
print('\n***********************\n')

#第二题
# 从测试集得到风速
velocity = int(input())
# 默认是0级
rank = 0
# 如果风速在74到95之间，输出1
####### begin #######
if velocity>=74 and velocity<=95:
    rank=1
####### end #########
# 如果风速在96到110之间，输出2
####### begin #######
elif velocity>=96 and velocity<=110:
    rank=2
####### end #########
# 如果风速在111到130之间，输出3
####### begin #######
elif velocity>=111 and velocity<=130:
    rank=3
####### end #########
# 如果风速在131到154之间，输出4
####### begin #######
elif velocity>=131 and velocity<=154:
    rank=4
####### end #########
# 如果风速大于155，输出5
####### begin #######
elif velocity>=155:
    rank=5
####### end #########
print(rank)
