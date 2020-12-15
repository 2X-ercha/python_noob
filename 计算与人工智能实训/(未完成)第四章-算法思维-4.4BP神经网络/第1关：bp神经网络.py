# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:27:53 2020

@author: hyr
"""

from sklearn.datasets import load_iris
import numpy as np

np.random.seed(0)
from csv import reader


def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            row_split = row[0].split('\t')
            row_float = list(map(float, row_split))
            dataset.append(row_float)
        return np.array(dataset)


def minMaxScaler(X):
    X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    return X_std


def label_trans(y_1d):  # 标签转换，将一维标签转换为三维
    label_dict = {0: [1, 0, 0], 1: [0, 1, 0], 2: [0, 0, 1]}
    y_3d = []
    for i in range(len(y_1d)):
        y_3d.append(label_dict[int(y_1d[i])])
    return np.array(y_3d)


def inv_label_trans(y_3d):  # 标签逆转换
    y_1d = []
    for i in range(y_3d.shape[0]):
        for j in range(y_3d.shape[1]):
            if (y_3d[i][j] == 1):
                y_1d.append(j)
                break
    return np.array(y_1d)


def shuffle(X, Y):
    lenX = len(X)
    random_sort = np.random.permutation(lenX)
    trainX = []
    trainY = []
    testX = []
    testY = []
    for i in range(lenX):  # 百分之80%用于训练，20%用于测试
        if i < lenX * 0.8:
            trainX.append(X[random_sort[i]])
            trainY.append(Y[random_sort[i]])
        else:
            testX.append(X[random_sort[i]])
            testY.append(Y[random_sort[i]])
    return np.array(trainX), np.array(trainY), np.array(testX), np.array(testY)


def sigmoid(x):  # 激活函数
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):  # 激活函数求导
    return sigmoid(x) * (1 - sigmoid(x))


def forward_propagate(an_input):
    # 计算并激活隐藏层
    for j in range(hidden_n):
        total = 0
        for i in range(input_n):
            total += an_input[i] * input_weights[j][i]
        total += input_weights[j][-1]  # 加入最后的偏置
        hidden_z[j] = total
        hidden_a[j] = sigmoid(hidden_z[j])
    # 计算并激活输出层
    ##########begin##############

    ############end################


def back_propagate(an_input, label, learn_rate):
    # 前向预测
    forward_propagate(an_input)
    # 求输出层神经单元误差
    output_deltas = [0] * output_n
    for k in range(output_n):
        error = output_a[k] - label[k]  # 误差
        output_deltas[k] = sigmoid_derivative(output_z[k]) * error

    # 求隐藏层神经单元误差
    ############begin#############

    ###########end#################

    # 更新隐藏单元权重
    for k in range(output_n):
        for j in range(hidden_n):
            hidden_weights[k][j] -= learn_rate * output_deltas[k] * hidden_a[j]
        hidden_weights[k][-1] -= learn_rate * output_deltas[k]

    # 更新输入权重
    ############begin##############

    #############end#############
    # 求全局误差
    error = 0
    for k in range(output_n):
        error += 0.5 * (label[k] - output_a[k]) ** 2
    return error


def train(X, Y, iterate=20, learn_rate=0.05):
    # 训练神经网络
    for t in range(iterate):
        error = 0
        for i in range(len(X)):
            error += back_propagate(X[i], Y[i], learn_rate)
        # 输出每次迭代的结果
        # print('iterate:',t,' the cost=',error)

        # print('Y True:',Y)
        y_pred_3d = predict(X)
        y_pred_1d = inv_label_trans(y_pred_3d)
        y_train_1d = inv_label_trans(Y)

        correct_rate = accuracy_score(y_pred_1d, y_train_1d)
        # print('the train accuracy:',correct_rate)


def predict(X):
    y_pred_result = []
    for i in range(len(X)):
        forward_propagate(X[i])
        # y_pred=output_a.copy()
        #        print('Y pred:',y_pred)
        y_pred = [0] * output_n
        maxOut = max(output_a)
        for j in range(output_n):
            if output_a[j] == maxOut:
                y_pred[j] = 1
            else:
                y_pred[j] = 0
        y_pred_result.append(y_pred)
    #       print('Y pred:',y_pred_3d)
    return np.array(y_pred_result)


def accuracy_score(y_pred_1d, y_test_1d):
    correct_number = 0
    test_number = len(y_pred_1d)
    for i in range(test_number):
        if y_pred_1d[i] == y_test_1d[i]:
            correct_number += 1
    return correct_number / test_number


input_n = 7  # 输入层
hidden_n = 6  # 隐藏层
output_n = 3  # 输出层

# 初始化
input_weights = np.random.rand(hidden_n, input_n + 1)  # 输入数据上的权值
hidden_weights = np.random.rand(output_n, hidden_n + 1)  # 隐藏单元上的权值

hidden_a = [1] * hidden_n  # 存放该神经元激活之后的值。
output_a = [1] * output_n

hidden_z = [1] * hidden_n  # 存放上一层的加权和值，未激活
output_z = [1] * output_n

filename = 'seeds_dataset.csv'
Dataset = load_csv(filename)

# iris=load_iris()
# X=iris.data
# 对X进行数据归一化
X = Dataset[:, :-1]
X = minMaxScaler(X)

y = Dataset[:, -1] - 1

# print(X[0:10])
# print(y[0:10])

Y = label_trans(y)

trainX, trainY, testX, testY = shuffle(X, Y)

train(trainX, trainY, 1000, 0.005)
y_pred_test = predict(testX)
y_pred_1d = inv_label_trans(y_pred_test)
y_test_1d = inv_label_trans(testY)
correct_rate = accuracy_score(y_pred_1d, y_test_1d)
print(correct_rate)
# print('correct_rate=',correct_rate)


# 编写bp神经网络分类任务中的前向信息传递和反向误差传播的代码。为后面使用深度学习工具时有个直观的理解
# 0.8