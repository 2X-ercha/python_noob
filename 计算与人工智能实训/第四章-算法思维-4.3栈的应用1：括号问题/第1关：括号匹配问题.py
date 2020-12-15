from queue import LifoQueue
#括号匹配
S=input() #输入的字符串
########## begin ##########
# 请在此填写代码
stack=LifoQueue(maxsize=0)
flag=True
for i in S:
    if i in ['(','[','{']:
        stack.put(i)
        continue
    if stack.empty():  #如果加入右括号时栈为空集，那必须停止，不然stack.get()会阻塞错误并不会报错，造成程序无法继续运行的结果
        flag=False
        break
    x=stack.get()
    if (i==')' and x != '(') or (i==']' and x != '[') or (i=='}' and x != '{'):
        flag=False
        break
if not stack.empty():flag=False
print(flag)
########## end ##########(