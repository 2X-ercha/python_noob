#coding=utf-8

#创建一个空列表numbers
numbers = []

#str用来存储输入的数字字符串，lst1是将输入的字符串用空格分割，存储为列表
str = input()
lst1 = str.split(' ')

#将输入的数字字符串转换为整型并赋值给numbers列表
for i in range(len(lst1)):
   numbers.append(int(lst1.pop()))

# 请在此添加函数plus的代码，函数参数为一个列表，对列表中的数值元素进行累加求和
#********** Begin *********#
def plus(l):
    return sum(l)
#********** End **********#

#调用plus函数，并将返回结果存储到变量d中
d = plus(numbers)
print(d)