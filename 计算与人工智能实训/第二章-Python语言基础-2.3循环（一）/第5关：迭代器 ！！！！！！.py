'''
任务描述
迭代器就是用来循环访问一系列元素。迭代器不仅可以迭代序列也可以迭代不是序列但是表现出序列行为的对象。

本关的任务是让读者理解与学会使用迭代器。

相关知识
迭代器的优点
迭代器访问与for循环访问非常相似，但是也有不同之处。对于支持随机访问的数据结构如元组和列表，迭代器并无优势，因为迭代器在访问的时候会丢失数据索引值，但是如果遇到无法随机访问的数据结构如集合时，迭代器是唯一访问元素的方式。
迭代器仅仅在访问到某个元素时才使用该元素，在这之前，元素可以不存在，所以迭代器很适用于迭代一些无法预先知道元素总数的巨大的集合。
迭代器提供了一个统一的访问集合的接口，定义iter()方法对象，就可以使用迭代器访问。
理解迭代器
可直接作用于for循环的数据类型如:list、tuple、dict等统称为可迭代对象:Iterable。可以使用方法isinstance()判断一个对象是否是可迭代对象。

例如:

from collections import Iterable
result = isinstance([],Iterable)
print(result)
result = isinstance((),Iterable)
print(result)
result = isinstance('python',Iterable)
print(result)
result = isinstance(213,Iterable)
print(result)
结果为:

True
True
True
False
可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator。next()函数访问每一个对象，直到对象访问完毕返回一个StopIteration异常。可以使用isinstance()判断一个对象是否是Iterator对象。
例如:

from collections import Iterator
result = isinstance([],Iterator)
print(result)
result = isinstance((),Iterator)
print(result)
result = isinstance((x for x in range(10)),Iterator)
print(result)
结果为:

False
False
True
所有的Iterable都可以通过iter()函数转化为Iterator。

定义迭代器
当自己定义迭代器时，需要定义一个类，类里面包含一个iter()函数，这个函数能够返回一个带next()方法的对象。
例如:

class MyIterable:
    def __iter__(self):
        return MyIterator()
class MyIterator:
    def __init__(self):
        self.num = 0
    def __next__(self):
        num += 1
        if self.num >= 10:
            raise StopIteration
        return self.num
复制迭代器
迭代器当一次迭代完毕后就结束了，在此调用便会引发StopIteration异常。如果想要将迭代器保存起来，可以使用复制的方法:copy.deepcopy():x = copy.deepcopy(y)，不可使用赋值的方法，这样是不起作用的。

如果你想了解更多运算符相关知识，请参考[美]Wesley J. Chun 著《Python核心编程》第八章。

编程要求
本关的编程任务是补全Book.py文件中的判断语句部分，具体要求如下：

当输入一个列表时，填入将列表List转换为迭代器的代码；
填入用next()函数遍历迭代器IterList的代码。
本关涉及的代码文件ListCalculate.py的代码框架如下:

List = []
member = input()
for i in member.split(','):
    result = i
    List.append(result)
#请在此添加代码，将List转换为迭代器的代码
#********** Begin *********#
#********** End **********#
while True:
    try:
        #请在此添加代码，用next()函数遍历IterList的代码
        #********** Begin *********#
        #********** End **********#
        result = int(num) * 2
        print(result)
    except StopIteration:
        break
测试说明
本文的测试文件是ListCalculate.py，具体测试过程如下：

平台自动编译生成ListCalculate.py；
平台运行ListCalculate.py，并以标准输入方式提供测试输入；
平台获取ListCalculate.py输出，并将其输出与预期输出对比。如果一致则测试通过，否则测试失败。
以下是平台对src/step4/ListCalculate.py的样例测试集：

预期输入：

5,6,7,8,9

预期输出：

10
12
14
16
18

预期输入：

12,54,89,10,0

预期输出：

24
108
178
20
0

'''

List = []
member = input()
for i in member.split(','):
    result = i
    List.append(result)
# 请在此添加代码，将List转换为迭代器的代码
# ********** Begin *********#
it=iter(List)
# ********** End **********#
while True:
    try:
        # 请在此添加代码，用next()函数遍历IterList的代码
        # ********** Begin *********#
        num=next(it)
        # ********** End **********#
        result = int(num) * 2
        print(result)
    except StopIteration:
        break


'''
引自于《菜鸟教程：迭代器与生成器》
###仅引用迭代器



迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：

实例(Python 3.0+)
>>> list=[1,2,3,4]
>>> it = iter(list)    # 创建迭代器对象
>>> print (next(it))   # 输出迭代器的下一个元素
1
>>> print (next(it))
2
>>>
迭代器对象可以使用常规for语句进行遍历：

实例(Python 3.0+)
#!/usr/bin/python3
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
执行以上程序，输出结果如下：

1 2 3 4
也可以使用 next() 函数：

实例(Python 3.0+)
#!/usr/bin/python3
 
import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
执行以上程序，输出结果如下：

1
2
3
4
创建一个迭代器
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。

如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。

更多内容查阅：Python3 面向对象

__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。

__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。

创建一个返回数字的迭代器，初始值为 1，逐步递增 1：

实例(Python 3.0+)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
执行输出结果为：

1
2
3
4
5
StopIteration
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

在 20 次迭代后停止执行：

实例(Python 3.0+)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)
执行输出结果为：

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20



'''