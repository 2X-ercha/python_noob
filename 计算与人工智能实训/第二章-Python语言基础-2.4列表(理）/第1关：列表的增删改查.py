# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:25:27 2020

@author: hyr
列表的增删改查
好友名单管理
"""
#建立初始名单
nameList=eval(input())

############begin###############
#1.请在好友名单尾部添加一个好友'曾海洋'
nameList.append('曾海洋')
############end#################

############begin############
#2.请在好友名单开头添加一个好友'胡波'
nameList.insert(0,'胡波')
##############end############

#############begin###########
#3.请将首个王姓好友的名字修改为'王仁'。
i=0
for x in nameList:
    if x.startswith('王'):
        break
    i+=1
nameList[i]='王仁'
#############end#############

############begin################
#4.删除首个赵姓好友
i=0
for x in nameList:
    if x.startswith('赵'):
        break
    i+=1
del nameList[i]
###########end#################

print(nameList)