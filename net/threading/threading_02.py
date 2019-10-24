import time
import threading
start_time = time.time()
def add(n):
     num = 0
     for i in range(n):
          num+=i
     print(num)

#IO密集型 计算密集型
# 下面两个函数 属于计算密集型(串行比并行快,因为只有一个线程不用切换)
# add(100000000)
# add(200000000)
# end_time = time.time()
# print(end_time-start_time)#耗时39.783562660217285


# 多线程调用
# #创建一个线程(多线程的时候 sellp不会阻塞cpu)
t1 = threading.Thread(target=add,args=(1000000000,))
t2 = threading.Thread(target=add,args=(2000000000,))
#执行线程
t1.start()
t2.start()
t1.join()# 等待当前线程完毕(阻塞当前线程)
t2.join()
end_time = time.time()
print(end_time-start_time)
# 耗时498.20162630081177(我操太慢了由此可见,计算密集型不适合使用所线程)

#GIL 同一时刻只能有一个线程进入cpu,所以为了实现高并发,python使用多进程