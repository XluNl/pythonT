import time
import threading
print('死锁')
start_time = time.time()
#lock= threading.Lock()
lock = threading.RLock()#避免死锁(递归锁,内部一个计数器acquire时相当于+1 release时-1)
def add():
     #acquire 和 release是成对出现的
     lock.acquire()
     print('ok')
     time.sleep()
     lock.acquire()
     print('ok1')
     lock.release()
     lock.release()


