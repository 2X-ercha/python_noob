import math

n = eval(input())
A = []
for i in range(n):
    x, y = map(int, input().split())
    A.append((x, y))


def Distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def Distance_x(a, b):
    return abs(a[0]-b[0])

def Distance_y(a, b):
    return abs(a[1]-b[1])

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
    for i in range(mid,low-1,-1):
        if Distance_x(A[i],A[mid])>d:break
        for j in range(mid+1,high+1):
            if Distance_x(A[i],A[j])>d:break
            if Distance_y(A[i],A[j])<=d:
                d=min(Distance(A[i],A[j]),d)
    return d
    ########## end ##########


A.sort()
result = FidMin(A, 0, len(A) - 1)
print('%.3f' % result)
