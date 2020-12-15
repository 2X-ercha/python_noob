# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:27:39 2020

@author: hyr
列表的排序
对一个班的学生的数学成绩进行排序，并进行简单的统
"""

scores=eval(input())#录入多名学生的成绩

#########begin############
#1. 请找出最高分并输出
maxscore=max(scores)
print(maxscore)
##########end############

###########begin###########
#2. 请找出最低分并输出
minscore=min(scores)
print(minscore)
###########end############

###########begin############
#3. 请求出班级平均分并输出(保留4位小数)
average=sum(scores)/len(scores)
print("{:.4f}".format(average))
###########end##############

############begin###########
#4.对分数进行升序排序并输出排序后的结果
scores.sort()
print(scores)
############end############