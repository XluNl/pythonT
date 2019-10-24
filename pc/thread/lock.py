#__author: xlu.com
#date : 2018/10/28
import threading
import random
import time

g_lock = threading.Lock()
g_money = 1000
g_totcont = 10 #指定生产10次就退出
g_count = 0
class Producer(threading.Thread):
    def run(self):
        global g_money
        global g_count
        global g_totcont
        while True:
            money = random.randint(100,1000)
            g_lock.acquire()
            if g_count >= g_totcont :
                g_lock.release()
                break #break 前一定要释放锁
            else:
                g_money+=money
                g_count+=1
                print('%s生成了%d元钱，剩余%d元钱'%(threading.current_thread(),money,g_money))
            g_lock.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global g_money
        global g_count
        global g_totcont
        while True:
            money = random.randint(100,1000)
            g_lock.acquire()
            if g_money >= money :
                g_money -= money
                print('%s消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,g_money))
                #g_lock.release() 注意锁必须加载外面，因为条件如果不对，那么遥远不能解锁，会造成死锁
            else:
                if g_count >= g_totcont:
                    #生产者生产了十次 已经没有可以消费的了，当前线程退出(这里写并不合理，如果消费者业务繁琐比较慢，那么还没消费完，现在退出不合理)
                    g_lock.release()
                    break
                print('%s消费者准备消费%d元钱，剩余%d元钱,不足！'%(threading.current_thread(),money,g_money))
            g_lock.release()
            time.sleep(0.5)

def main():
    for item in range(1):
        t = Consumer(name='消费者%d'%(item))
        t.start()
    for item in range(1):
        t = Producer(name='生产者%d'%(item))
        t.start()

if __name__ == '__main__':
    main()