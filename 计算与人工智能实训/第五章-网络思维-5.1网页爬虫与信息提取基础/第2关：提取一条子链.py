# -*- coding: utf-8 -*-

import requests

# 湖南大学本科招生信息网中分数线网页URL：
url = 'http://admi.hnu.edu.cn/zsxx/tzgg.htm'  # 录取分数线网页URL
home = 'http://admi.hnu.edu.cn'

r = requests.get(url)  # 按照类文件的方式打开网页
r.encoding = r.apparent_encoding   #设置字符串的编码方式

def step2():
    # 建立空列表urls，来保存子网页的url
    urls = []
    # 请按下面的注释提示添加代码，完成相应功能
    #********** Begin *********#
    # 提取2020到2018每一年录取分数线子网站地址添加到urls列表中
    html = r.text
    url_index = html.find("湖南大学2020年各省各批次分数线陆续公布")
    for i in range(100):
        if html.find("href=",url_index-i,url_index) != -1:
            start = html.find("href=",url_index-i,url_index) + 8
            break
    for i in range(100):
        if html.find("htm",start,start+i) != -1:
            end=start+i
            break
    urls.append(home+html[start:end])
    #********** End **********#
    return urls