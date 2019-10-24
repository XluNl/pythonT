print('协程')

import time

def xiaofei(tag):
     print('.......staing,%s',tag)
     while True:
         baozi = yield tag
         print('%s第%s个包子'%(tag,baozi))
def shch():
    next(x1)
    next(x2)
    num = 0
    while num<5:
        num+=1
        print('包子',num)
        t = x1.send(num)
        t1=x2.send(num)
        print(t,t1)

if __name__ == '__main__':
    x1 = xiaofei('shch1')
    x2 = xiaofei('shch2')
    p = shch()



