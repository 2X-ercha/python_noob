# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:05:47 2019

@author: Administrator
"""
# 豆瓣电影排行榜
import requests
from bs4 import BeautifulSoup

# 豆瓣电影排行榜
url = "https://movie.douban.com/chart"
# 文件名
filename = 'douban.txt'
# 请求网页
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
r = requests.get(url, headers=headers)


def gettitle(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = []
    briefs = []
    # 请按下面的注释提示添加代码，完成相应功能
    ###### Begin ######
    # 1.先获取影片标题和链接，再由链接得到影片简介，最后将影片标题和简介分别存放在titles和briefs列表中
    data = soup.find_all('a', {'class': 'nbg'})
    for a in data:
        titles.append(a.attrs['title'])
        href = a.attrs['href']
        briefs.append(getdetail(href))
    return titles, briefs
    ####### End #######
    # 先获取影片标题和链接，再由链接得到影片简介，最后将影片标题和简介加入到links列表中


def getdetail(href):
    # 请按下面的注释提示添加代码，完成相应功能
    ###### Begin ######
    # 2.由排行榜上的影片链接进入影片详情页面，获取影片简介并返回
    r = requests.get(href, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    brief = soup.find('span', {'property': 'v:summary'}).text.strip().replace(' ', '').replace('\n', '')
    return brief
    ####### End #######


def savefile(titles, briefs, filename):
    # 请按下面的注释提示添加代码，完成相应功能
    ###### Begin ######
    # 3.将影片标题和简介按指定格式保存到文本文件
    count = 1
    f = open(filename, 'w', encoding='utf-8')
    for title, brief in zip(titles, briefs):
        f.write("{:}>{}\n{}\n".format(count, title, brief))
        count = count + 1
    f.close()
    ####### End #######


titles, briefs = gettitle(r.text)
savefile(titles, briefs, filename)