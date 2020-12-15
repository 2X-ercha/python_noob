import math

n = eval(input())
A = []
for i in range(n * 2):
    group = 1 if i < n else 2
    x, y = map(int, input().split())
    A.append((x, y, group))


def Distance(a, b):
    if a[2]==b[2]:return 1e8
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def Distance_x(a, b):
    return abs(a[0]-b[0])

# 求[low..high]区间内的最小点距
def FidMin(A, low, high):
    ########## begin ##########
    # 请在此填写代码，返回区间[low,high]的最小点距
    if high-low==1:return Distance(A[low],A[high])
    if high==low:return 1e8
    mid = (low + high) // 2
    FidMin_left=FidMin(A,low,mid)  # 左区间最小
    FidMin_right=FidMin(A,mid+1,high)  # 右区间最小
    d=min(FidMin_left,FidMin_right)
    left,right=[],[]
    for i in range(mid-1,low-1,-1):
        if Distance_x(A[i],A[mid])<=d:
            left.append(i)
        else:break
    for i in range(mid+1,high+1):
        if Distance_x(A[i],A[mid])<=d:
           right.append(i)
        else:break
    left.append(mid)
    for x in left:
        for y in right:
            if Distance(A[x],A[y])<d:d=Distance(A[x],A[y])
    return d
    ########## end ##########


A.sort()
result = FidMin(A, 0, len(A) - 1)
print('%.3f' % result)