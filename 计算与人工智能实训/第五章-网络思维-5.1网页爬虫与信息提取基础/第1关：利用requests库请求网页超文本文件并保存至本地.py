# -*- coding: utf-8 -*-
import requests
import os

# 湖南大学本科招生信息网中招生章程网页URL：
url = 'http://admi.hnu.edu.cn/zsxx/zszc1.htm'  # 招生章程网页URL

def step1():
    # 请按下面的注释提示添加代码，完成相应功能
    #********** Begin *********#
    # 1.将网页内容保存到r
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    # 2.将读r.text以文本文件模式写入以学号命名的 “hnu.txt” 文件：
    with open("hnu.txt","w") as f1:
        f1.write(r.text)
    #********** End **********#
