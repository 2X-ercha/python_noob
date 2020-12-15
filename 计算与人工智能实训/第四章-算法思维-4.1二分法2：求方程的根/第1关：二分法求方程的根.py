import numpy as np
E = 1e-6
########## begin ##########
# 请在此填写代码, 计算6*np.exp(x)-113*x+17=0的根
def f(x):
    return 6*np.exp(x)-113*x+17

def bin_search(a,b):
    while a<=b:
        mid=(a+b)/2
        if abs(f(mid))<=E:
            return mid
        if f(a)*f(mid)<=0:b=mid
        else:a=mid
    return mid

print("{:.4f}".format(bin_search(0,1)))
print("{:.4f}".format(bin_search(4,5)))
########## end ##########