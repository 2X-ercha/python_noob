''' O(n)=nlogn '''
n = eval(input())
A = list(map(float, input().split()))


# 求A[low..high]中跨越mid的最大子序列积
def FindMaxCrossing(A, low, mid, high):
    ########## begin ##########
    # 请在此填写代码，返回通过mid的最大序列积
    leftpro = 0
    pro0 = 1
    for i in range(mid, low - 1, -1): #从mid向左乘
        pro0 *= A[i]
        if pro0 > leftpro: #保证左部分最大
            leftpro = pro0
    rightpro = 0
    pro0 = 1
    for i in range(mid + 1, high + 1): #从mid向右乘
        pro0 *= A[i]
        if pro0 > rightpro: #保证右部分最大
            rightpro = pro0
    return leftpro * rightpro ##由于从mid向两边取，保证了连续性和最大##

    ########## end ##########


# 求A[low..high]中的最大子序列积
def FidMax(A, low, high):
    ########## begin ##########
    # 请在此填写代码，返回区间[low,high]的最大子序列积
    if low == high: return A[low]
    mid = (low + high) // 2
    leftpro = FidMax(A, low, mid)
    rightpro = FidMax(A, mid + 1, high)
    crosspro = FindMaxCrossing(A, low, mid, high)
    return max(leftpro, rightpro, crosspro) #左积右积不包含mid或边界为mid，crossmid则跨越mid，保证结果的完整准确
    ########## end ##########

result = FidMax(A, 0, len(A) - 1)
print('%.2f' % result)

'''
直接采用DP的方式，我想我只能下意识的打出O(n)的算法，也就是采用遍历mid的方式进行状态转移
觉得自己又更菜了2333
'''