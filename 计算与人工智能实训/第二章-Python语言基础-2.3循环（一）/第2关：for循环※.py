# 第一题
L = [101, 25, 38, 29, 108, 121]
N = len(L)
miu = sum(L)/N
s2 = 0
####### Begin #########
# 请在此输入for循环表达式
for x in L:
####### End ########
     s2 = s2+(x-miu)**2
sigma=(s2/N)**0.5
print(sigma)

# 第二题
####### Begin #########
# 请在此输入for循环表达式
for x in range(100,999,1):
####### End ########
    x1 = x%10       #取出x的个位
    x2 = x//10%10   #取出x的十位
    x3 = x//100     #取出x的百位
    if x1**3+x2**3+x3**3==x:
        print(x)