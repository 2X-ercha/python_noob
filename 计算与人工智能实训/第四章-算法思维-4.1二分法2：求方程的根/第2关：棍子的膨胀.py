import math

L, n, C = map(float, input().split())
E = 1e-8
S=(1+n*C)*L
########## begin ##########
# 请在此填写代码，求方程的根
def f(h):
    r=(4*h**2+L**2)/(8*h)
    s=2*r*math.asin(L/(2*r))
    return s-S

def bin_search(a,b):
    while a<=b:
        mid=(a+b)/2
        if abs(f(mid))<=E:
            return mid
        if f(a)*f(mid)<=0:b=mid
        else:a=mid
    return mid

########## end ##########
h=bin_search(0.00001,L/2)
print('%.4f' % h)