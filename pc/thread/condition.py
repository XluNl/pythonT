#__author: xlu.com
#date : 2018/10/28
import threading
import random
import time

g_Condition = threading.Condition()
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
            g_Condition.acquire()
            if g_count >= g_totcont :
                g_Condition.release()
                break #break 前一定要释放锁
            else:
                g_money+=money
                g_count+=1
                g_Condition.notify_all() #每次生产完毕都通知所有等待的消费者
                print('%s生成了%d元钱，剩余%d元钱'%(threading.current_thread(),money,g_money))
            g_Condition.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global g_money
        global g_count
        global g_totcont
        while True:
            money = random.randint(100,1000)
            g_Condition.acquire()
            while g_money < money :
                if g_count >= g_totcont:
                    g_Condition.release()
                    return
                g_Condition.wait()#while循环的意思 ，接到通知后，线程苏醒去排队获取锁,继续判断只要钱钱不够 则继续阻塞等待
                #g_lock.release() 注意锁必须加载外面，因为条件如果不对，那么遥远不能解锁，会造成死锁
            g_money -= money
            print('%s消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,g_money))
            g_Condition.release()
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