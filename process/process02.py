print('多进程')

#进程模块
#import  multiprocessing\
from  multiprocessing import  Process
import  time
import os

class Myprocess(Process):
    def __init__(self,name):
        super(Myprocess,self).__init__()
        #self.name = name

    def run(self):
        #os.getppid() 父进程id
        #os.getpid() 子进程id
        print(self.name,os.getpid(),os.getppid())
def run(name):
    #time.sleep(2)
    print('1232',name)

#windows 下必须加下面这句
if __name__ == '__main__':
     p_list = []
     for p in range(5):
         p = Myprocess('clp')
         p_list.append(p)
         p.start()
     # for p in p_list:
     p.join() #这里如果使用join 则主进程会等待子进程全部执行完毕 再执行
     print('end')
