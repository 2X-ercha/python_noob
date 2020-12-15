n = eval(input())
A = []
for i in range(n):
    X = A.append(list(map(int, input().split())))

DP = [[10000000000000000000000000000000000000000000000000000000000000] * (i + 1) for i in range(n)]


def MinRouteProd(i, j):
    ########## begin ##########
    # 请在此填写代码，返回以i,j为顶点的最小路径积
    DP[0][0] = A[0][0]
    for a in range(i, n - 1):
        for b in range(j, a + 1):
            DP[a + 1][b] = min(DP[a + 1][b], DP[a][b] * A[a + 1][b])
            DP[a + 1][b + 1] = min(DP[a + 1][b + 1], DP[a][b] * A[a + 1][b + 1])
    result = min(DP[n - 1])
    ########## end ##########
    return result


print(MinRouteProd(0, 0))