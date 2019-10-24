#__author: xlu.com
#date : 2019/10/16

from gevent import monkey
import gevent
import time

# 最大程度 切换协程
monkey.patch_all()

def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m',time.ctime())
    gevent.sleep(2)
    # time.sleep(2);
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m',time.ctime())

def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m',time.ctime())
    gevent.sleep(1)
    # time.sleep(2);
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m',time.ctime())


if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(func1),
        gevent.spawn(func2),
        #gevent.spawn(func3),
    ])