'''
字典和列表一样，都是Python中十分重要的可变容器模型，都可以存储任意类型元素，我们将以菜单的例子来说明字典使用的基本知识。

餐馆的菜单上不仅包含菜名，菜名后面还必须包含该道菜的价格。如果要用列表实现，就需要两个列表，例如：

list_menu = ['fish','pork','potato','noodles']
list_price = [40,30,15,10]

给定一个菜名，要查找相应的价格，就先要在list_menu中找到相应的位置，再在list_price中找到相应的价格，这种方式效率低下，那么我们是否可以将菜名和价格都存储在一个可变容器中呢，答案是可以的。

在本关中，我们将学习掌握能够将相关信息关联起来的Python字典的相关知识，并完成对包含菜名和价格的菜单的处理操作。

相关知识
字典是Python最强大的数据类型之一，通过键-值对的方式建立数据对象之间的映射关系。字典的每个键-值对用冒号:分割，每个键-值对间用逗号,分隔开，字典是包含在{}中。列表格式如下：

d = { key1 : value1, key2 : value2 }

每个键都与一个值相关联，我们可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。

访问字典中的值
要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：

# 创建并初始化menu字典
menu = {'fish':40, 'pork':30, 'potato':15, 'noodles':10}
# 获取并返回menu字典中键'fish'键对应的值
print(menu['fish'])
输出结果：
40

添加键-值对
字典是一种动态数据结构，可随时在字典中添加键—值对。要添加键—值对时，可依次指定字典名、键和键对应的值。

下面在字典menu中添加两道菜的菜名和价格：

# 创建并初始化menu字典
menu = {'fish':40, 'pork':30, 'potato':15, 'noodles':10}
# 向menu字典中添加菜名和价格
menu['juice'] = 12
menu['egg'] = 5
#输出新的menu
print(menu)
输出结果：
{'fish': 40,'pork': 30,'potato': 15,'noodles': 10, 'juice': 12,'egg': 5}

新的menu字典包含6个键-值对，新增加的两个键-值对（菜名和对应价格）添加在了原有键-值对的后面，注意字典中键-值对的排列顺序和添加顺序没有必然联系，Python不关心字典中键-值对的排列顺序，而只关心键与值得对应关系。

同理，字典和列表一样，可以先创建一个空字典，然后可以不断向里面添加新的键-值对。

修改字典中的值
字典和列表一样，里面的值都是可以修改的。要修改字典中的值，可直接指定字典中的键所对应的新值。例如，将menu中的fish价格改为50。

# 创建并初始化menu字典
menu = {'fish':40, 'pork':30, 'potato':15, 'noodles':10}
# 修改menu字典中菜fish的价格
menu['fish'] = 50
# 打印输出新的menu
print(menu)
输出结果：
{'fish': 50, 'pork': 30, 'potato': 15, 'noodles': 10}

删除键-值对
我们可以通过del方法删除字典中不需要的键-值对，使用del方法时，要指定字典名和要删除的键。

例如，在menu菜单中删除键noodles和它的值。

# 创建并初始化menu字典
menu = {'fish':40, 'pork':30, 'potato':15, 'noodles':10}
# 删除noodles键值对
del menu['noodles']
# 打印输出新的menu
print(menu)
输出结果：
{'fish': 40, 'pork': 30, 'potato': 15}

如果您想了解更多有关列表使用知识，请参考:【美】Eric Matthes著《Python编程——从入门到实践》第六章。

编程要求
本关的编程任务是补全src/Step2/menu.py文件的代码，实现相应的功能。具体要求如下:

向menu_dict字典中添加一道菜名lamb，它的价格是50；

获取menu_dict字典中的fish的价格并打印出来；

将menu_dict字典中的fish的价格改为100；

删除menu_dict字典中noodles这道菜；

输出新的menu_dict菜单。

本关涉及的代码文件src/Step2/menu.py的代码框架如下：

# coding=utf-8
# 创建并初始化munu_dict字典
menu_dict = {}
while True:
    try:
        food = input()
        price = int(input())
        menu_dict[food]= price
    except:
        break
#请在此添加代码，实现对menu_dict的添加、查找、修改等操作，并打印输出相应的值
###### Begin ######
#######  End #######
测试说明
本关的测试文件是src/Step2/menu.py，测试过程如下：

平台自动编译并运行menu.py，并以标准输入方式提供测试输入；

平台获取程序输出，并将其输出与预期输出对比。如果一致则测试通过，否则测试失败。

以下是平台对src/Step2/menu.py的样例测试集：

测试输入：

pizza
40
noodles
30
carrot
20
turkey
34
fish
37
预期输出：

37
{'pizza': 40, 'carrot': 20, 'turkey': 34, 'fish': 100, 'lamb': 50}
'''


# coding=utf-8

# 创建并初始化menu_dict字典
menu_dict = {}
while True:
    try:
        food = input()
        price = int(input())
        menu_dict[food]= price
    except:
        break

#请在此添加代码，实现对menu_dict的添加、查找、修改等操作，并打印输出相应的值
###### Begin ######
menu_dict['lamb']=50
print(menu_dict['fish'])
menu_dict['fish']=100
del menu_dict['noodles']
print(menu_dict)
#######  End #######
