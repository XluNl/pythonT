print('多进程')

#进程模块
#import  multiprocessing\
from  multiprocessing import  Process
import  time
def run(name):
    #time.sleep(2)
    print('1232',name)
if __name__ == '__main__':
     p_list = []
     for p in range(5):
         p = Process(target=run,args=('clp',))
         p_list.append(p)
         p.start()
     # for p in p_list:
     p.join() #这里如果使用join 则主进程会等待子进程全部执行完毕 再执行
     print('end')
# 多进程(主进程)
# 多进程(1)
# 1232 clp
# 多进程(2)
# 1232 clp
# 多进程(3)
# 1232 clp
# end