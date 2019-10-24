print('进程队列-Pipe')

#进程模块
#import  multiprocessing\
from  multiprocessing import  Process,Queue,Pipe

import  time
import os
def run(conn):
    #time.sleep(2)
    conn.send('yubu')
    print(conn.recv())
    conn.close()

#windows 下必须加下面这句
if __name__ == '__main__':
    #创建一个队列
     pr_con,chia_con = Pipe()
     #print(pr_con,chia_con)
     p = Process(target=run,args=(chia_con,))
     p.start()
     #主进程发送一个消息
     pr_con.send('3333')
     #主进程等待子进程响应
     p.join()
     print('end')
     print(pr_con.recv())
