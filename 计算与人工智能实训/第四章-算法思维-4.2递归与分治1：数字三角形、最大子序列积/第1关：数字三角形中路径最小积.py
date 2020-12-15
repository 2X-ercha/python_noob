'''
两种打法其实是一样的（这题用递归的本质其实也是DP），只不过————
我他喵的怎么傻到忘记可以把函数当数组用啊！！！
为什么我要字典套元组啊！！！
递归那么简单我为什么要用DP啊
'''


#DP写法#

n = eval(input())
A = []
for i in range(n):
    X = A.append(list(map(int, input().split())))
A_min={}
def MinRouteProd1(i, j):
    ########## begin ##########
    # 请在此填写代码，返回以i,j为顶点的最小路径积
    for a in range(i,n):
        for b in range(j,a+1):
            A_min[(a,b)]=100000000000000000000000000000000000
    A_min[(0,0)]=A[0][0]
    for a in range(i,n-1):
        for b in range(j,a+1):
            A_min[(a+1,b)]=min(A_min[(a+1,b)],A_min[(a,b)]*A[a+1][b])
            A_min[(a+1,b+1)]=min(A_min[(a+1,b+1)],A_min[(a,b)]*A[a+1][b+1])
    result=100000000000000000000000000000000
    for a in range(n):
        result=min(A_min[(n-1,a)],result)
    ########## end ##########
    return result

print(MinRouteProd1(0, 0))


#递归写法#

n = eval(input())
A = []
for i in range(n):
    X = A.append(list(map(int, input().split())))
def MinRouteProd2(i, j):
    ########## begin ##########
    # 请在此填写代码，返回以i,j为顶点的最小路径积
    if i==n-1:
        result = A[i][j]
    else:
        result = min(MinRouteProd2(i+1,j),MinRouteProd2(i+1,j+1))*A[i][j]
    ########## end ##########
    return result


print(MinRouteProd2(0, 0))