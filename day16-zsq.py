import time
print('装饰器(函数) 实现在不更改方法内容的情况下,获取每个方法执行的时间')

def add_log(tag=1):
	def showtime(f):
		def func():
			start = time.time()
			f()
			end = time.time()
			if tag==1:
				print(f,end-start)
		return func
	return showtime

#@后面接收的是一个返回值(一个方法的指针)
@add_log() #foot = showtime(foot)
def foot():
	time.sleep(2)

@add_log() #boot = showtime(boot)
def boot():
	time.sleep(3)

foot()
boot()



