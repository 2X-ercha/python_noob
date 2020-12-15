# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 07:44:05 2020

@author: hyr
"""

def binary_search_3(A, x):
    ###############begin################
    #返回整数x在列表A中出现的次数
    a,b=0,len(A)-1
    while a<b:
        mid=(a+b)//2
        if A[a]<=x<=A[mid]:b=mid
        else:a=mid+1
    p1,b=a,len(A)-1
    a=p1
    while a<b:
        mid=(a+b)//2
        if A[mid+1]<=x<=A[b]:a=mid+1
        else:b=mid
    p2=b
    return p2-p1+1
    ##############end####################


