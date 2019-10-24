print('条件变量-实现线程间的通信')

import threading,time
from  random import randint
# 自定义一个线程类(继承 Thread)
class boss(threading.Thread):
    def run(self):
        print('boos,今晚加班')
        event.is_set() or event.set()
        time.sleep(5)
        print('boos:22:00可以下班了')
        event.is_set() or event.set()
class work(threading.Thread):
    def run(self):
        # 如果是work 先抢到线程 则会阻塞(wait默认为false)
        event.wait()
        print('work,哎--要加班')
        time.sleep(2)
        event.clear()
        event.wait()
        print('work:yes')

if __name__ == '__main__':
    # 创建一个 条件锁
    #Event.isset() 返回状态值
    #Event.wait() Event.isset()==Flase 则会阻塞线程
    #Event.set() 设置event状态为true
    #Event.clear() 设置event的状态为false
    event = threading.Event()#默认是lock()
    thrs = []
    # 装包子
    L = []
    # 创建5个生产者
    for t in range(5):
        thrs.append(work())
    # 添加一个消费者
    thrs.append(boss())
    for t in thrs:
        t.start()
    for t in thrs:
        t.join()

