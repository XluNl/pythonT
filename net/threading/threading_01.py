import time
import threading
start_time = time.time()
def foo(n):
     print('foo%s'%n)
     time.sleep(2)#sellp 不占用cup
     print('end foo')
def bar(n):
     print('bar%s'%n)
     time.sleep(1)
     print('end bar')
#当前调用的两个方法 都在一个线程里(sleep会阻塞)
#串行调用
# foo(2)
# bar(3)
#耗时:3.0018951892852783

# 多线程调用
# #创建一个线程(多线程的时候 sellp不会阻塞cpu)
t1 = threading.Thread(target=foo,args=(2,))
t2 = threading.Thread(target=bar,args=(3,))
#执行线程
t1.start()
t2.start()
print('主线程')

end_time = time.time()
print(end_time-start_time)
#耗时:0.0009975433349609375
