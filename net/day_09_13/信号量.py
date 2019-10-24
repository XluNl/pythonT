print('信号量')

import threading,time
# 也是一把锁 一次只放5个线程进入锁空间
bounded = threading.BoundedSemaphore(5)
# 自定义一个线程类(继承 Thread)
class myThreding(threading.Thread):
    def run(self):
        if bounded.acquire():
            print(self.name)
            time.sleep(3)
            bounded.release()

if __name__ == '__main__':
    thrs = []
    for t in range(8):
        thrs.append(myThreding())

    for t in thrs:
        t.start()

