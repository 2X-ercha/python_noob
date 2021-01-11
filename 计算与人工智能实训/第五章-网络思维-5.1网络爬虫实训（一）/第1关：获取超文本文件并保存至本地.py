# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:36:53 2020

@author: Administrator
"""

import requests

# 湖南大学首页
url = "http://www.hnu.edu.cn/"

# 文件名
filename = 'hnu.txt'


def gethtml(url):


    # 请按下面的注释提示添加代码，完成相应功能
    ###### Begin ######
    # 1.获取网页文件并返回
    h = requests.get(url)
    h.encoding = "utf-8"
    return h.text
    ####### End #######

def saveinfo(html, filename):
    with open(filename,"w", encoding='utf-8') as f:
        f.write(html)

# 请按下面的注释提示添加代码，完成相应功能
###### Begin ######
# 2.将html保存到文件文件

####### End #######

html = gethtml(url)
saveinfo(html, filename)
