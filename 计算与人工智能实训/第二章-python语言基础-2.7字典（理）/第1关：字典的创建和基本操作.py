# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:36:42 2020

@author: Administrator
"""

# 创建并初始化score_dict字典
score_dict = {}
for i in range(5):
    # 请按下面的注释提示添加代码，完成相应功能
    #1.对score_dict字典进行初始化，数据从键盘输入，得到如任务描述中的字典
    ###### Begin ######
    a=input()
    b=input()
    if b.isdigit():b=eval(b)
    score_dict[a]=b
    #######  End #######


# 请按下面的注释提示添加代码，完成相应功能
#2.请在此添加代码，实现对score_dict的添加、删除、查找、修改等操作，并打印输出相应的值
###### Begin ######
score_dict['体育']=90
flag=False
for key in score_dict.keys():
    if key=='化学':flag=True
if flag:print(score_dict['化学'])
else:print('不存在')
score_dict['语文']=100
del score_dict['信息']
print(score_dict)
#######  End #######