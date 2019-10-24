print('进程队列-Queue')

#进程模块
#import  multiprocessing\
from  multiprocessing import  Process,Queue

import  time
import os

def run(q):
    #time.sleep(2)
    q.put(['www',123])
    print('subid=',id(q))

#windows 下必须加下面这句
if __name__ == '__main__':
    #创建一个队列
     q = Queue()
     print('mainid=',id(q))
     p_list = []
     for p in range(3):
         p = Process(target=run,args=(q,))
         p_list.append(p)
         p.start()
     # for p in p_list:
     # p.join() #这里如果使用join 则主进程会等待子进程全部执行完毕 再执行
     print('end')
     print(q.get())# get的时候就会阻塞,直到有值才会往下走
     print(q.get())
     print(q.get())
    #主进程皮一下
     run(q)
