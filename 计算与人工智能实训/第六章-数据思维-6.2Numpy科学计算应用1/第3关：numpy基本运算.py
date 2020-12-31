import numpy as np


# 注意，以下对行号和列号的描述都从0开始，例如，最开始的行是第0行
def func1(arr1, arr2):
    ########## begin ##########
    # 请在此填写代码，计算矩阵arr1和arr2的点乘，其中arr1的列数和arr2的行数相同
    return arr1.dot(arr2)
    ########## end ##########


def func2(arr1, arr2):
    ########## begin ##########
    # 请在此填写代码，计算矩阵arr1和arr2的星乘，其中arr1和arr2的形状相同
    return arr1 * arr2
    ########## end ##########


def func3(arr):
    ########## begin ##########
    # 请在此填写代码，对数组arr, 计算并返回所有元素的最大值
    return np.max(arr)
    ########## end ##########


def func4(arr):
    ########## begin ##########
    # 请在此填写代码，对数组arr, 计算每一行的最小值，以数组的形式返回
    return np.min(arr, axis=0)
    ########## end ##########


def func5(arr):
    ########## begin ##########
    # 请在此填写代码，对数组arr, 计算每个元素的正弦函数结果，以新的数组形式返回
    return np.sin(arr)
    ########## end ##########