#__author: xlu.com
#date : 2018/10/28

from queue import Queue
# from threading import Thread
import time
import threading
import json
import random

#理解 queue是线程安全的  用来代替多线程间，资源争夺，全局变量带来的安全问题
def main():
    q = Queue(10)
    for item in range(10):
        q.put(item) #默认block=True 如果队列已满 则会一直等待
    print(q.qsize()) #判断队列大小
    print(q.full()) #判断队列是否已满

    for it in range(10):
        print(q.get(block=True)) #默认block=True 如果没有值则会一直阻塞

if __name__ == '__main__':
    main()