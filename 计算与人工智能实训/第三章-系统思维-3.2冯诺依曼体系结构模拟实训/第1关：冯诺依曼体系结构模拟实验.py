# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:20:45 2020

@author: hzh
"""

#冯诺依曼体系结构模拟实验
#读程序指令
file = open('sys/step1/instruction1.txt', 'r')
#将指令存入存储器
mem = [instr for instr in file.readlines()]

#初始化程序计数器
IP = 0
#初始化指令寄存器
IR = ''
#初始化运算器
Reg= 0

#顺序执行每条指令
while True:
    IR = mem[IP]
    IP += 1
    ########## begin ##########
    code=IR.split()
    if len(code)==2:
        if code[0]=='000001': #读取
            ip=int(code[1],2)
            Reg=int(mem[ip][6:],2)
        elif code[0]=='000010': #储存
            mem[int(code[1],2)]='000000'+bin(Reg)
        elif code[0]=='000011': #加法
            ip=int(code[1],2)
            Reg+=int(mem[ip][6:],2)
        elif code[0]=='000100': #乘法
            ip=int(code[1], 2)
            Reg*=int(mem[ip][6:],2)
        elif code[0]=='000101': #打印
            ip=int(code[1], 2)
            print(int(mem[ip][6:],2))
    elif code[0]=='000110': #结束
        break

    ########## end ##########

'''

mem=[
'000001 0000001000',
'000100 0000001001',
'000011 0000001010',
'000100 0000001000',
'000011 0000001011',
'000010 0000001100',
'000101 0000001100',
'000110',
'0000000000000011',
'0000000000001000',
'0000000000000010',
'0000000000000110',
'0'
]
#初始化程序计数器
IP = 0
#初始化指令寄存器
IR = ''
#初始化运算器
Reg= 0
#顺序执行每条指令
while True:
    IR = mem[IP]
    IP += 1
    code=IR.split()
    if len(code)==2:
        if code[0]=='000001': #读取
            ip=int(code[1],2)
            Reg=int(mem[ip][6:],2)
        elif code[0]=='000010': #储存
            mem[int(code[1],2)]='000000'+bin(Reg)
        elif code[0]=='000011': #加法
            ip=int(code[1],2)
            Reg+=int(mem[ip][6:],2)
        elif code[0]=='000100': #乘法
            ip=int(code[1], 2)
            Reg*=int(mem[ip][6:],2)
        elif code[0]=='000101': #打印
            ip=int(code[1], 2)
            print(int(mem[ip][6:],2))
    elif code[0]=='000110': #结束
        break

'''