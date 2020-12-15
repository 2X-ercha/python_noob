# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:32:01 2020

@author: hyr
列表索引切片
对学生成绩进行降序排序，输出前三名的成绩，以及后三名的成绩，以及去掉一个最高的去掉一个最低分之后的成绩均值。
"""

#已录入的10名学生的成绩
scores=eval(input())#录入多名学生的成绩

##########begin###########
#请对scores进行降序排序
scores.sort(reverse=True)
##########end#############
print(scores)

#########begin############
#请找出前三名(降序)的成绩赋给变量firstThree
firstThree=scores[:3]
##########end############
print(firstThree)

###########begin###########
#请找出后三名(降序)的成绩赋给变量lastThree
lastThree=scores[-3:]
###########end############
print(lastThree)

###########begin############
#请求出去掉一个最高分以及去掉一个最低分之后的成绩均值赋给变量averge
scores.pop(0)
scores.pop(-1)
average=sum(scores)/len(scores)
###########end##############
print("{:.4f}".format(average))