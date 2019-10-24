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

@show_time
def text(num):
    inde = 0;
    for i in range(num):
        inde+=i
    print("inde= %s" % inde)


if __name__ == "__main__":
    text(10000)