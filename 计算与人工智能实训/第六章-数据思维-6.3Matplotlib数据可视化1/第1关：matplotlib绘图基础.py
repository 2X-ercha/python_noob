import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'simHei'  # 显示汉字
plt.rcParams['axes.unicode_minus'] = False  # 显示负号


def DrawLine(output_name):
    x = np.arange(0, 2 * np.pi, 0.1)
    y1 = np.sin(x)
    y2 = np.sin(x * 2)
    plt.figure('fig1')
    ########## begin ##########
    # 请在此填写代码，分别使用数据(x,y1)和(x,y2)绘制线图
    plt.title('不同周期正弦曲线')
    plt.plot(x,y1,'r-',label = '2π周期')
    plt.plot(x,y2,'b-',label = 'π周期')
    plt.xlabel('自变量')
    plt.ylabel('因变量')
    plt.legend(loc = 'upper right')
    plt.savefig(output_name)
    # plt.show()
    ########## end ##########


def DrawPie(output_name):
    sales = [1528, 796, 543, 1046, 865]  # 手机店上月各品牌手机销量
    brands = ['华为', 'vivo', 'oppo', '小米', '苹果']  # 品牌列表
    plt.figure('fig2')
    ########## begin ##########
    # 请在此填写代码，绘制手机销量的饼图
    plt.title('手机销量')
    plt.pie(sales,[0.1, 0, 0, 0, 0],brands,autopct='%2.1f%%')
    plt.savefig(output_name)
    # plt.show()
    ########## end ##########


def DrawBar(output_name):
    avg_scores = np.array([80.54, 78.46, 74.68, 82.35])  # 各班考试平均分
    class_name = ['机械1班', '机械2班', '电气1班', '电气2班']
    plt.figure('fig3')
    ########## begin ##########
    # 请在此填写代码，绘制各班平均成绩的条形图
    plt.bar(class_name, avg_scores)
    plt.xlabel('班级')
    plt.ylabel('平均成绩')
    plt.savefig(output_name)
    # plt.show()
    ########## end ##########


DrawLine('1-fig1.png')
DrawPie('1-fig2.png')
DrawBar('1-fig3.png')