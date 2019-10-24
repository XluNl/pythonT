print('队列在单线程下没有意义,是为多线程而生')

import threading,time,queue
from  random import randint
 #创建一个队列
q = queue.Queue(3)#默认是0 无限大
q.put('clp')
q.put('zzz')
q.put('ssss')#若果数量大于允许的数量 则会阻塞主,直到列表被取出
#q.put('sss',0)#这样设置 直接会抛出错误

# 队列先进先出
print(q.get())
print(q.get())
print(q.get())
#print(q.get())#这里也会阻塞直到有新的内容加入进来
print(q.get(0))#这里会直接抛出错误