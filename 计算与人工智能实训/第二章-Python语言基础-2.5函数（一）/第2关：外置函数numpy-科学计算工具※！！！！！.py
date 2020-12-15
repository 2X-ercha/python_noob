'''
我们在进行科学公式计算编程过程中会用到很多科学函数，但是我们不用担心不会用，因为在Python中存在一个非常强大的工具Numpy，下面过程中使用Numpy三角函数作为引子，带领大家了解Numpy库与Python中的画图工具。

Numpy函数的导入
Numpy的函数的导入只需要在最开始引入Numpy然后命名即可，在后续的使用中就可以直接引用函数，示范如下：

import numpy as np

这样就导入了numpy库，后续只需要np.xx函数既可以使用xx函数。

Numpy函数
Numpy所带的函数非常多，下面只左右砖头来引美玉，更多的美玉可以直接参考Numpy的说明文档。

linspace函数
linespace函数的完整形态如下：

linespace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

参数：

start：scalar类型（这不是一个具体的数据类型，而是指某一些数据类型，比如int,float,bool,long,str等等都属于sclar类型）。这个数参数表示这个序列的开始值。

stop：scalar类型。如果endpoint=True。那么stop就是序列的终止数值。当endpoint=False时，返回值中不包含最后一个端点，并且步长会改变。

num：int型，可选参数，默认值为50。表示要生成的样本数，必须是非负值。

endpoint：bool类型。可选参数，默认值为True，这时stop就是最后的样本。为False时，不包含stop的值。

retstep：bool类型。可选参数，默认值为True，这时返回值是(samples,step)，前面的是数组，后面是步长。

dtype：表示输出的数组的数据类型，如果没有给出就从其他输入中推断输出的类型。

返回值：

samples：ndarray类型。在[start，stop]闭区间，或者[start，stop)半闭合区间中，数量为num，步长相等的样本。

step：float类型。可选。只有restep参数取值为True时才会返回这个返回值，表示样本中步长。

下面来看一个示范：

import numpy as np
a,b = np.linspace(1, 50, 10, False, True)
print(a)
print(b)
输出如下：

[ 1.   5.9 10.8 15.7 20.6 25.5 30.4 35.3 40.2 45.1]
4.9
此输出表明，返回的是不包含右闭区间均匀分布的十个样本数，其中样本数的步长为4.9

sin()函数
此函数的完整形态为sin(a)，用来求正弦。

如果a为ndarray对象，则np.sin(a) 对矩阵a中每个元素取正弦。

如果a是单个数据值，则np.sin(a) 对a元素取正弦。

例如：

a = [np.pi,np.pi/2,np.pi/4]
b = np.pi
print(np.sin(a))
print(np.sin(b))
[  1.22464680e-16   1.00000000e+00   7.07106781e-01]
1.22464679915e-16
在输出中可以看到，对列表求正弦，则返回列表。对具体数字求正弦，则直接返回其值。

cos()函数
此函数的完整形态为cos(a)，用来求余弦。

如果a为ndarray对象，则np.cos(a) 对矩阵a中每个元素取余弦。

如果a是单个数据值，则np.sin(a) 对a元素取余弦。

下面来看一个整体的例子：

import numpy as np
a = np.array([0, 30, 45, 60, 90])
print('数组中角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print(np.sin(a * np.pi / 180))
print('数组中角度的余弦值：')
print(np.cos(a * np.pi / 180))
数组中角度的正弦值：
[0.         0.5        0.70710678 0.8660254  1.        ]
数组中角度的余弦值：
[1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01
 6.12323400e-17]

 编程要求
本关的编程任务是补全右侧文件Begin-End处的代码，实现相应的功能。具体要求如下：

第一题：

绘制如下函数组的曲线（花形）,角度属于[0, 2pi]。
x=sin(10θ)cos(θ)

y=sin(10θ)sin(θ)

第二题

绘制如下函数的函数型曲线，角度属于[0, 2pi]。
x=16(sinθ)
3


y=13cosθ−5cos2θ−2cos3θ−cos4θ

'''

import matplotlib
import numpy as np

#matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 第一题
#x = sin(10\theta)cos(\theta)
#y = sin(10\theta)sin(\theta)
theta=np.linspace(0, 2*np.pi, 1000)
############ begin ##########
# 求出2pi区间下均匀分布的1000个点
x=theta
############ end ############
y=np.sin(10*theta)*np.sin(theta)
plt.plot(x, y, 'r')
#plt.savefig('./src/step4/ans1/轨迹1.png')
plt.show()
print(x[0])
plt.close()


# 第2题
# 求2pi区间下均匀分布的100个点
t = np.linspace(0, 2*np.pi, 100)
x =16*np.sin(t)**3
# 求y值，并直接输出
############ begin ##########
y =13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
############ end ############
print(y[0])
plt.plot(x, y, 'r')
plt.axis([-25, 25, -20, 15])
#plt.savefig('./src/step4/ans1/轨迹2.png')
plt.show()
plt.close()