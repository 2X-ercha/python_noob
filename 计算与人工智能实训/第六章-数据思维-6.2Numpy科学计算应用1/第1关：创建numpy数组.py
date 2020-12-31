import numpy as np
#1 使用numpy的linspace函数，创建初值为1，终止为5，元素个数为20的等差数组
########## begin ##########
# 请在此填写代码
A=np.linspace(1,5,20)
########## end ##########


#2 将数组B变换成2行5列的二维数组
B=np.arange(0,20,2)
# 请在此填写代码
B=B.reshape(2,5)
########## end ##########


#3 随机数种子为7，生成4行3列的随机数数组，值在[0,1)之间
np.random.seed(7)
# 请在此填写代码
C=np.random.rand(4,3)
########## end ##########

#4 随机数种子为11，生成3行4列的正态分布随机数数组，期望值为5，标准差为2
np.random.seed(7)
# 请在此填写代码
D=2*np.random.randn(3,4)+5
########## end ##########

#5 将数组D的内容写入文本文件,使用英文分号为分隔符，浮点数精确到小数点后5位，文件名为1.txt
# 请在此填写代码
# arr2=np.loadtxt('2.csv', delimiter=',')  ##  构造
np.savetxt('1.txt', D, fmt='%.5f', delimiter=';')  ##  存储

########## end ##########


#6 使用斐波那契数列(1,1,2,3,5,...)生成一个5行4列的numpy数组，数组名为E
# 请在此填写代码
l = [1,1]
for i in range(2,20):
    l.append(l[i-1]+l[i-2])
E = np.array(l)
E = E.reshape(5,4)

########## end ##########