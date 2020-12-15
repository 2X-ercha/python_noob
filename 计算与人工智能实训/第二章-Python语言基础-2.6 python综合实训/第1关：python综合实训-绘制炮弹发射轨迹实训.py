# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:48:07 2020

@author: hzh
"""
import numpy as np
import matplotlib.pyplot as plt
def calBombTrace(theta):
    v0, g, n = 300, 9.8, 30         #v0初速度，n个时间点
    theta_d = np.radians(theta)     #因numpy中cos、sin的输入为弧度值，故先将theta从度转换为弧度
    v0_x = v0*np.cos(theta_d)       #炮弹水平初速度
    v0_y = v0*np.sin(theta_d)       #炮弹垂直初速度
    tmax = 2*v0_y/g                 #落地时间，即v0_y*t-0.5gtt=0的解
    ############# begin #########
    #获得n个时刻的横/纵坐标
    t=np.linspace(0,tmax,n)
    xt=v0_x*t
    yt=v0_y*t-1/2*g*t**2
    ########### end #############
    return xt, yt

for theta in [30, 45, 60, 75]:
    ############ begin #########
    # 调用函数，得到theta返回的值，并存储到xt与yt变量
    xt,yt=calBombTrace(theta)
    ########### end #############
    plt.plot(xt, yt)

plt.grid('on')
plt.axis([0, 10000, 0, 5000])
plt.show()
#plt.savefig('轨迹.png')
plt.close()
print([round(x,6) for x in xt])
print([round(x,6) for x in yt])
