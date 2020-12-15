# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:36:42 2020

@author: Administrator
"""

# 创建空列表score_dict
score_dict = {}
# 每次循环生成一个键值对
for i in range(3):
    # 输入课程名作为字典的键
    key = input()
    # 创建空列表
    value_list = []
    # 请按下面的注释提示添加代码，完成相应功能
    # 1.从键盘输入两个分数，保存到列表中
    ###### Begin ######
    for j in range(2):
        value_list.append(eval(input()))
    #######  End #######
    score_dict[key] = value_list

print(score_dict)

# 创建空列表score_list
score_list = []
# 每次循环生成一个字典
for i in range(2):
    # 创建空字典
    s_dict = {}
    # 请按下面的注释提示添加代码，完成相应功能
    # 2.对从键盘输入三门课程及成绩，保存到字典中
    ###### Begin ######
    for j in range(3):
        a=input()
        s_dict[a] = eval(input())
    #######  End #######
    score_list.append(s_dict)

print(score_list)