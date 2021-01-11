# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:36:53 2020

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.hnu.edu.cn/"

filename = 'hnu.txt'


def gethtml(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def gettitle(html):
    # 请按下面的注释提示添加代码，完成相应功能
    ###### Begin ######
    # 1.解析网页，获取湖大首页上的新闻标题和链接,分别放入titles和hrefs列表
    soup = BeautifulSoup(html,"html.parser")
    titles, hrefs = [], []
    newslist = soup.select( ".hdxw-right > ul > li > a")
    for new in newslist:
        titles.append(new.get("title"))
        hrefs.append(new.get("href"))
    ####### End #######
    return titles, hrefs


def saveinfo(titles, hrefs, filename):
    # 请按下面的注释提示添加代码，完成相应功能
    ###### Begin ######
    # 2.将titles和hrefs列表中的内容保存到文件文件
    with open(filename, "w", encoding="utf-8") as f:
        for i,j in zip(titles, hrefs):
            f.write(i+"\n"+j+"\n")
    ####### End #######

html = gethtml(url)
titles,hrefs=gettitle(html)
saveinfo(titles, hrefs, filename)
