print('条件变量-实现线程间的通信')

import threading,time
from  random import randint
# 也是一把锁 一次只放5个线程进入锁空间
#wait() 条件不满足是调用(释放锁)
# notify() 激活一个线程(通常是通知被阻塞的线程wait)
# notifyall()
# lock()
# RLock()
# 自定义一个线程类(继承 Thread)
class shchan(threading.Thread):
    def run(self):
        global L
        while True:
            val = randint(0,100)
            print('生产者',self.name,"append"+str(val),L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)
class xiaofei(threading.Thread):
    def run(self):
        global L
        while True:
            # 当线程被唤醒时 会从这里开始执行
            lock_con.acquire()
            if len(L)==0:
                #如果 没有包子则先阻塞,知道生产者通知有包子了 再往下执行
                lock_con.wait()
            print('消费者',self.name,"delete"+str(L[0]),L)
            del L[0]
            lock_con.release()
            #0.1s 吃一个包子
            time.sleep(0.1)
if __name__ == '__main__':
    # 创建一个 条件锁
    lock_con = threading.Condition()#默认是lock()
    thrs = []
    # 装包子
    L = []
    # 创建5个生产者
    for t in range(5):
        thrs.append(shchan())
    # 添加一个消费者
    thrs.append(xiaofei())
    for t in thrs:
        t.start()
    # for t in thrs:
    #     t.join()

