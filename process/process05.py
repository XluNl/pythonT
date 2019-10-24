print('进程队列-Queue')

#进程模块
#import  multiprocessing\
from  multiprocessing import  Process,Queue,Manager

import  time
import os

def run(d,l,i):
    #time.sleep(2)
    d[i] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(i)
    #print(l)

#windows 下必须加下面这句
if __name__ == '__main__':
    #创建一个队列
     with Manager() as manager:
         d = manager.dict()
         l = manager.list(range(5))
         p_list = []
         for i in range(10):
            p = Process(target=run,args=(d,l,i))
            p.start()
            p_list.append(p)

         for p in p_list:
            p.join() #这里如果使用join 则主进程会等待子进程全部执行完毕 再执行

         print(d)
         print(l)

