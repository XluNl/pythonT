print('队列在单线程下没有意义,是为多线程而生')

import threading,time,queue
from  random import randint

class shchan(threading.Thread):
    def run(self):
        while True:
            val = randint(0,100)
            q.put(val)
            print('生产包子%s号'%val)
            time.sleep(1)
class xiaofei(threading.Thread):
    def run(self):
        while True:
            re = q.get()
            print('吃掉包子%s号'%re)

if __name__ == '__main__':
    # 创建一个 条件锁
    q = queue.Queue(10)
    thrs = [shchan(),shchan(),shchan(),shchan(),xiaofei()]

    # 有了队列 就不需要锁了,当比如吃饱的时候,没有包子,则会阻塞直到有包子出现
    for t in thrs:
        t.start()


