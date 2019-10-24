import time
import threading
print('同步锁')
start_time = time.time()
lock= threading.Lock()
#
bounded = threading.BoundedSemaphore(5)
def add():
     global num
     #枷锁(局部枷锁)
     print('ok')#这里会提示打印出来
     lock.acquire()
     tmp = num
     time.sleep(3)
     print('ok1')
     num = tmp-1 #这样如果不枷锁 永远都是99,因为0.1对于cpu来讲时间太长了,每次来就只好借覆盖了
     #解锁
     lock.release()
     #num-=1
     #print(num)
#num 为全局变量
num = 100
ts_list = []
for t in range(10):
     h = threading.Thread(target=add)
     h.start()
     ts_list.append(h)

for i in ts_list:
     i.join()
#i.join()

print(num)
#执行线程
if __name__ == '__main__':
     end_time = time.time()
     print(end_time-start_time)

#同步锁 与 GIL的关系
