import time
import threading
print('进程是一个资=资源包')
start_time = time.time()
def add(n):
     num = 0
     for i in range(n):
          num+=i
     print(threading.current_thread())
     print(num)

t1 = threading.Thread(target=add,args=(100000,))
t2 = threading.Thread(target=add,args=(200000,))
ts = []
ts.append(t1)
ts.append(t2)
for t in ts:
     # 注意setDaemon 必须在start之前设置
     t.setDaemon(True)#守护线程(主线程结束之后 子线程也就玩完)
     t.start()

# 等待t2 执行完毕后再回到主线程执行
t.join()#这样用在python里面不出错,会把for循环最后一次的值否只给t,所以这个t=t2
#执行线程
if __name__ == '__main__':
     end_time = time.time()
     print(end_time-start_time)
     print(__name__)