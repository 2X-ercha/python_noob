# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:36:42 2020

@author: Administrator
"""

# 创建并初始化score_dict字典
score_list=['姓名','语文','英语','数学','体育']
# 请按下面的注释提示添加代码，完成相应功能
#1.根据上面的列表创建score_dict字典并初始化，得到如任务描述中的字典，字典中的值从键盘输入
###### Begin ######
score_dict={}
for i in range(5):
    value=input()
    if value.isdigit():value=eval(value)
    score_dict[score_list[i]]=value
#######  End #######


# 请按下面的注释提示添加代码，完成相应功能
#2.请在此添加代码，计算张三同学的总分，并将总分作为新的键值对加入，最后输出score_dict的所有键值对
###### Begin ######
sum=0
for key,value in score_dict.items():
    print("{} {}".format(key,value))
    if type(value)==int or type(value)==float:sum+=value
print("总分 {}".format(sum))
#######  End #######