# coding=utf-8

# 创建并初始化Guests列表
guests = []
while True:
    try:
        guest = input()
        guests.append(guest)
    except:
        break

# 请在此添加代码，对guests列表进行插入、删除等操作
###### Begin ######
deleted_guest = guests[-1]
guests.insert(2, deleted_guest)
guests.pop()
guests.pop(1)
print(deleted_guest)
print(guests)

#######  End #######
