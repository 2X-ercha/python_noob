'''
Python字典中包含大量数据，字典和列表一样，支持遍历操作。Python有多种遍历字典的方式，可以遍历字典的所有键-值对，键或值。

例如：餐馆的菜单包含了菜名和价格等信息，餐馆需要将菜名和价格都展示给顾客，但也有些时候只需要将菜名都展示给厨师，还有些时候只需要将价格展示给收银员。这三种情况就用到了字典不同的遍历方式。

本关的目标是让读者掌握字典遍历的相关知识和用法，需要基于这些知识实现对菜单不同的查找和展示处理。

相关知识
遍历字典中的键-值对
Python为字典类型提供了items()方法，items()方法会将字典里的所有的键与值一起返回，

例如，餐馆有一个菜单包含了菜名和价格信息。菜名和价格顾客都需要知道，可以通过遍历输出menu字典的键和值来实现。

#coding = utf-8
# 创建并初始化menu菜单字典
menu={'fish':'40','pork':'30','potato':'20','lamb':'50'}
# 利用items()方法遍历输出键和值
for key,value in menu.items():
    print('\nkey:'+key)
    print('value:'+value)
输出结果：

key:fish
value:40
key:pork
value:30
key:potato
value:20
key:lamb
value:50
输出结果表示，items()方法每次都将对应的键和值指定到key和value变量中，然后用for循环输出。

遍历字典中的键
对于餐馆中的厨师来说，他们并不想要知道菜的价格，只需要知道菜名然后将其做出来就行。所以对于厨师来说，我们需要遍历menu字典中的所有菜名。

Python为字典类型内置了keys()方法，该方法会将字典里的键遍历出来，例如：

# 创建并初始化menu菜单字典
menu={'fish':'40','pork':'30','potato':'20','lamb':'50'}
# 利用keys()方法遍历输出键
for key in menu.keys():
    print('food_name:'+key)
输出结果：
food_name:fish
food_name:pork
food_name:potato
food_name:lamb

输出结果表示，keys()方法每次都是将menu菜单中的键输出，显示菜名。

遍历字典中的值
对于餐馆中的收银员来说，他们可能并不想知道菜单的菜名，只需要知道菜的价格然后收账即可。所以对于收银员来说，我们需要遍历menu字典中的所有菜的价格。

Python为字典类型内置了values()方法，该方法会将字典里的值遍历出来，例如：

# 创建并初始化menu菜单字典
menu={'fish':'40','pork':'30','potato':'20','lamb':'50'}
# 利用values()方法遍历输出值
for value in menu.values():
    print('food_price:'+value)
输出结果：
food_price:40
food_price:30
food_price:20
food_price:50

输出结果表示，values()方法每次都是将menu菜单中的值输出，显示菜的价格。

如果您想了解更多有关字典使用知识，请参考:【美】Eric Matthes著《Python编程——从入门到实践》第六章。

编程要求
本关的编程任务是补全src/Step3/key-values.py文件的代码，实现相应的功能。具体要求如下：

将menu_dict菜单的键遍历输出；

将menu_dict菜单的值遍历输出；

本关涉及的代码文件src/Step3/key_values.py的代码框架如下：

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
#请在此添加代码，实现对menu_dict的遍历操作并打印输出键与值
###### Begin ######
#######  End #######
测试说明
本关的测试文件是src/Step3/key_values.py，测试过程如下：

平台自动编译并运行key_values.py，并以标准输入方式提供测试输入；

平台获取程序输出，并将其输出与预期输出对比。如果一致则测试通过，否则测试失败。

以下是平台对src/Step3/key_values.py的样例测试集：

测试输入：

Spring Rolls
40
pork
30
Fried Wonton
15
预期输出：

Spring Rolls
pork
Fried Wonton
40
30
15
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

#请在此添加代码，实现对menu_dict的遍历操作并打印输出键与值
###### Begin ######
for key in menu_dict.keys():
    print(key)
for value in menu_dict.values():
    print(value)
#######  End #######



