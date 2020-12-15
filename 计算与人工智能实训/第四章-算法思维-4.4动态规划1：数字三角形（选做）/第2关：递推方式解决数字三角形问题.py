n = eval(input())
A=[]
for i in range(n):
    X = A.append(list(map(int, input().split())))

DP=[[-1]*(i+1) for i in range(n)]

#进行递推求解
for i in range(n):
    DP[n-1][i]=A[n-1][i]

for i in range(n-1,0,-1): #层循环
    ########## begin ##########
    # 请在此填写代码，返回以i,j为顶点的最小路径积
    for j in range(i):
        DP[i-1][j]=A[i-1][j]*min(DP[i][j],DP[i][j+1])
    ########## end ##########


print(DP[0][0]) #结果在DP[0][0]中