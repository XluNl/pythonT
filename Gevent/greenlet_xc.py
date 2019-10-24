#__author: xlu.com
#date : 2019/10/16

import Gevent
from  greenlet import greenlet

def con1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()

def con2():
    print(3)
    gr1.switch()  #switch 相当于next或send
    print(4)


if __name__ == "__main__":
    gr1 = greenlet(con1)
    print(gr1)
    gr2 = greenlet(con2)
    gr1.switch()