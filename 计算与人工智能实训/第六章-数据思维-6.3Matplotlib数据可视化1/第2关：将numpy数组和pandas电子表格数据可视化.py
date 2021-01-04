import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.rcParams['font.family'] = 'simHei'  # 显示汉字
plt.rcParams['axes.unicode_minus'] = False  # 显示负号


# input_name:输入的excel文件名
# output_name:输出的图片文件名
def DrawLine(input_name, output_name):
    plt.figure('fig1')
    ########## begin ##########
    # 请在此填写代码，绘制开盘价和收盘价的线图，日期为横轴
    data = pd.read_excel(input_name)
    x = data['日期']
    y1 = data['开盘']
    y2 = data['收盘']
    plt.title('开盘价与收盘价对比图')
    plt.plot(x, y1, 'b-v', label = '开盘价')
    plt.plot(x, y2, 'r-v', label = '收盘价')
    plt.legend(loc = 'upper right')
    plt.xlabel('日期')
    plt.ylabel('股价')
    plt.savefig(output_name)
    ########## end ##########


# input_name:输入的csv文件名
# output_name:输出的图片文件名
def DrawBar(input_name, output_name):
    plt.figure('fig2')
    ########## begin ##########
    # 请在此填写代码，绘制各年度的国内生产总值的条形图
    data = np.loadtxt(input_name, delimiter = ',')
    x = [int(arr[0]) for arr in data]
    y = [arr[1] for arr in data]
    plt.bar(x, y)
    plt.xlabel('年度')
    plt.ylabel('国内生产总值')
    plt.savefig(output_name)
    ########## end ##########