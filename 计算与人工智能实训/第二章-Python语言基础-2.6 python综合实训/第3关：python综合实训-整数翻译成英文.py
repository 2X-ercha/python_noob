# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:47:23 2020
#整数翻译为英文的程序
@author: hzh
"""

def unit_to_word(u):  # 将0～9的数字转换成英文，并返回转换后的英文
    # 请在下面编写代码
    # ********** Begin ********** #
    dict0_9=['zero','one','two','three','four','five','six','seven','eight','nine']
    return dict0_9[u]
    # ********** End ********** #
    # 请不要修改下面的代码


def tens_to_word(t):  # 利用unit_to_word，将10～19、以及20～99的十位部分数字转换成英文，并返回转换后的英文
    # 请在下面编写代码
    # ********** Begin ********** #
    dict10_19=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    dict20_90_10=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    if 10<=t<20:return dict10_19[t-10]
    elif t%10!=0:return dict20_90_10[t//10]+' '+unit_to_word(t%10)
    else:return dict20_90_10[t//10]
    # ********** End ********** #
    # 请不要修改下面的代码

def hundreds_to_word(h):  # 利用unit_to_word、tens_to_word进行转换，并返回转换后结果的函数
    # 请在下面编写代码
    # ********** Begin ********** #
    if h<10:return unit_to_word(h)
    elif h<100:return tens_to_word(h)
    elif h%100==0:return unit_to_word(h//100)+' hundred'
    elif h%100//10==0:return unit_to_word(h//100)+' hundred and '+unit_to_word(h%10)
    else:return unit_to_word(h//100)+' hundred and '+tens_to_word(h%100)
    # ********** End ********** #
    # 请不要修改下面的代码

for test in [0, 5, 19, 23, 100, 700, 711, 729]:
    print(test, "=>", hundreds_to_word(test))
print('\n***********************\n')
