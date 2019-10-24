#__author: xlu.com
#date : 2019/7/27
import time

def text(num):
    inde = 0;
    for i in range(num):
        inde+=i
    print("inde= %s" % inde)

def show_time(fun):
    start_time = time.time()
    fun();
    end_time = time.time()
    print("sp= %s" % str(end_time-start_time))

def show(fun):
    def ret(par):
        print("par= %s" % par)
        start_time = time.time()
        fun(par);
        end_time = time.time()
        print("sp= %s" % str(end_time-start_time))
    return ret
if __name__ == "__main__":
    # show_time(text)
    text =  show(text)
    text(10)
