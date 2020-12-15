from queue import Queue
#加密
S=input()
key=input()
queue_ = Queue()
for c in key:queue_.put(c)
result=''
########## begin ##########
for i in S:
    x=queue_.get()
    result+=chr(ord(i)+int(x))
    queue_.put(x)
########## end ##########
print(result)