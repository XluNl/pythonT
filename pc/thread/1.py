#__author: xlu.com
#date : 2018/8/10

import threading
import process
import time

G_VALUE = 0
glock = threading.Lock()
# 多线程共享全局变量
def text():
    global G_VALUE
    glock.acquire()
    for item in range(1000000):
        # glock.acquire()
        G_VALUE += 1
        if G_VALUE >= 2000000:
            return
        # print(G_VALUE)
        # print(threading.current_thread())
    glock.release()
    print(G_VALUE)
    print(threading.current_thread())

rh1 = threading.Thread(target=text)
rh2 = threading.Thread(target=text)
rh3 = threading.Thread(target=text)
rh4 = threading.Thread(target=text)

rh1.start()
rh2.start()
rh3.start()
rh4.start()