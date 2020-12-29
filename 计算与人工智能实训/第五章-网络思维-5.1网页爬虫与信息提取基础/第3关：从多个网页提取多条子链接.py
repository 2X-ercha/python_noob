# -*- coding: utf-8 -*-

import requests

# 湖南大学本科招生信息网中通知公告网页URL：
url1 = 'http://admi.hnu.edu.cn/zsxx.htm'  # 通知公告网页URL
url2 = 'http://admi.hnu.edu.cn/zsxx/'
home = 'http://admi.hnu.edu.cn/'


def step22():
    firstpage = True  # 第一页标记
    # 建立空列表urls，来保存子网页的url
    urls = []
    year = 2020
    for page in range(17):
        # 请按下面的注释提示添加代码，完成相应功能
        # ********** Begin *********#
        # 提取2020到2018每一年录取分数线子网站地址添加到urls列表中
        if firstpage:
            r = requests.get(url1)
            firstpage = False
        else:
            r = requests.get(url2 + str(page) + '.htm')
        r.encoding = r.apparent_encoding
        html = r.text
        string = "湖南大学"+str(year)+"年各省各批次分数线陆续公布"
        url_index = html.find(string)
        if url_index != -1:
            for i in range(100):
                if html.find("href=", url_index - i, url_index) != -1:
                    start = html.find("href=", url_index - i, url_index) + 6
                    if page: start += 3
                    else: year=2017
                    break
            for i in range(100):
                if html.find("htm", start, start + i) != -1:
                    end = start + i
                    break
            urls.append(home + html[start:end])
            year += 1
        if year == 2020:break
        # ********** End **********#
    return urls