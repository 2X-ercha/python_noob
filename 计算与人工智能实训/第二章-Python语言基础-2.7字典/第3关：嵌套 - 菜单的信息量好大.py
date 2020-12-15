'''
Python的列表和字典可以存储任意类型的元素，所以我们可以将字典存储在列表中，也可以将列表存储在字典中，这种操作称为嵌套。

例如，餐馆中的菜单不仅仅包含菜名和价格，可能还会包含很多其他信息，这时候我们可能就需要采取嵌套的存储方式。

本关任务是让学习者利用嵌套方式存储菜单，让读者掌握Python嵌套的基本操作。

相关知识
列表中存储字典
餐馆中已经有了3份菜单，每份菜单都会有菜名和价格，我们要将这些信息存储在一起，可以采取如下方法。

将3份菜单用字典的方式存储菜名和价格，然后将这3份菜单字典存储在一个列表中，例如：

# 创建3个菜单字典，包含菜名和价格
menu1 = {'fish':40, 'pork':30, 'potato':20,'noodles':15}
menu2 = {'chicken':30, 'corn':55, 'lamb':65,'onion':12}
menu3 = {'bacon':36, 'beaf':48, 'crab':72,'eggs':7}
# 将3个菜单字典存储到列表menu_total中
menu_total = [menu1,menu2,menu3]
# 输出列表
print(menu_total)
输出结果：

[{'fish': 40, 'pork': 30, 'potato': 20, 'noodles': 15}, {'chicken': 30, 'corn': 55, 'lamb': 65, 'onion': 12}, {'bacon': 36, 'beaf': 48, 'crab': 72, 'eggs': 7}]

字典中存储列表
我们也可以在字典中存储列表，比如我们对于一份菜单，菜名作为键，而值我们想是这道菜的配料，那么我们就可以将这些配料作为列表存储，然后作为值存储在字典中。例如：

# 初始化menu菜单，里面包含配料列表
menu = {'fish':['vinegar','soy','salt'], 'pork':['sugar','wine']}
# 输出pork这道菜的配料
print('The burding of pork is:',menu['pork'])
输出结果：

The burding of pork is: ['sugar', 'wine']

字典中存储字典
我们也可以在字典中存储字典，例如我们有一份总菜单，包含2个子菜单，每个子菜单都包含菜名和价格。例如：

# 创建一个字典menu_sum，里面包含两个子菜单字典menu1和menu2
menu_sum = {
    'menu1':{'fish':40, 'pork':30, 'potato':20,'noodles':15},
    'menu2':{'chicken':30, 'corn':55, 'lamb':65,'onion':12}
}
# 输出menu1和menu2中的菜名和价格
print(menu_sum['menu1'])
print(menu_sum['menu2'])
输出结果：

{'fish': 40, 'pork': 30, 'potato': 20, 'noodles': 15}
{'chicken': 30, 'corn': 55, 'lamb': 65, 'onion': 12}

如果您想了解更多有关字典使用知识，请参考:【美】Eric Matthes著《Python编程——从入门到实践》第六章。

编程要求
本关的编程任务是补全src/Step4/menu_nest.py文件的代码，实现相应的功能。具体要求如下：

menu_total列表中初始时只包含menu1字典，menu1字典中包含两道菜和两道菜的价格；

编程要求是向menu_total列表中添加另外一个菜单字典menu2，menu2菜单中的菜名和menu1菜单一样，菜的价格是menu1菜的价格的2倍；

输出新的menu_total列表。

本关涉及的代码文件src/Step4/menu_nest.py的代码框架如下：

# coding=utf-8
# 初始化menu1字典，输入两道菜的价格
menu1 = {}
menu1['fish']=input()
menu1['pork']=input()
# menu_total列表现在只包含menu1字典
menu_total = [menu1]
# 请在此添加代码，实现编程要求
###### Begin ######
###### End ######
# 输出menu_total列表
print(menu_total)
测试说明
本关的测试文件是src/Step4/menu_nest.py，测试过程如下：

平台自动编译运行menu_nest.py，并以标准输入方式提供测试输入；

平台获取程序输出，并将其输出与预期输出对比。如果一致则测试通过，否则测试失败。

以下是平台对src/Step4/menu_nest.py的样例测试集：

测试输入：
40
30
预期输出：
[{'fish': 40, 'pork': 30}, {'fish': 80, 'pork': 60}]
'''

#coding=utf-8

#初始化menu1字典，输入两道菜的价格
menu1 = {}
menu1['fish']=int(input())
menu1['pork']=int(input())

#menu_total列表现在只包含menu1字典
menu_total = [menu1]

# 请在此添加代码，实现编程要求
#********** Begin *********#
menu2={}
for key,value in menu1.items():
    menu2[key]=value*2
menu_total.append(menu2)
#********** End **********#

#输出menu_total列表
print(menu_total)