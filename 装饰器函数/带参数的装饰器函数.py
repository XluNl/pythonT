#__author: xlu.com
#date : 2019/7/27

import time

def show_time(fun):
        def ret(parms):
            print("par= %s" % parms)
            start_time = time.time()
            fun(parms);
            end_time = time.time()
            print("sp= %s" % str(end_time-start_time))
        return ret

def log_d(tag=0):
    def show_time(fun):
        def ret(parms):
            print("par= %s" % parms)
            start_time = time.time()
            fun(parms);
            end_time = time.time()
            if(tag==1):
                print("sp= %s" % str(end_time-start_time))
        return ret
    #注意一定要返回哦
    return show_time

#相当于 text = log(1)(text)
@log_d(1)
def text(num):
    inde = 0;
    for i in range(num):
        inde+=i
    print("inde= %s" % inde)


if __name__ == "__main__":
    text(10000000)

