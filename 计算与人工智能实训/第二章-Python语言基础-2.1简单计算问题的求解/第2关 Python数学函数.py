from math import *

import math


def print_(x):
    if type(x) == float:
        print("%.4f" % x)
    else:
        print(x)
# ********** Begin ********** #
#请在每一题的print语句内完成题目所需的表达式

#第一题
print_(math.pi**4+math.pi**5)
print_(math.e**6)
print_(math.pi**4+math.pi**5-math.e**6)

#第二题
print_(math.pi/4)
print_(4*math.atan(1/5)-atan(1/239))

#第三题
print_(math.cos(2*math.pi/17))
print_(1/16*(-1+math.sqrt(17)+math.sqrt(2*(17-math.sqrt(17)))+2*math.sqrt(17+3*math.sqrt(17)-math.sqrt(2*(17-math.sqrt(17)))-2*math.sqrt(2*(17+math.sqrt(17))))))
print_(math.cos(2*math.pi/17)-1/16*(-1+math.sqrt(17)+math.sqrt(2*(17-math.sqrt(17)))+2*math.sqrt(17+3*math.sqrt(17)-math.sqrt(2*(17-math.sqrt(17)))-2*math.sqrt(2*(17+math.sqrt(17))))))

#第四题
print_(math.sqrt((1+math.sqrt(5))/2+2)-(1+math.sqrt(5))/2)

#第五题
print_(math.sinh(0.25))
print_((math.e**0.25-math.e**(-0.25))/2)

# ********** End ********** #