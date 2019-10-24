print('生成器->列表生成器:结论:生成器都是迭代器,迭代器不一定是生成器')
print(__name__)
# 列表生成 将for循环里的每个*2 放进一个列表
# a = [x*2 for x in range(10)]
# print(a) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#方式2
# def func(x):
# 	return x**3
# #可以传入一个函数
# a= [func(x) for x in range(10)]
# print(a) #[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

#快捷赋值方式
# b = [2,5]
# z,s = b #左右变得数量必须相等
# print(z,s) #z=2,s=5

#生成器(只返回一个生成器对象)
# s = (x*2 for x in range(10)) #此时的s 只是个生成器对象,并没有生成数据
# print(s) #<generator object <genexpr> at 0x000001DEA6B9B4C0>,生成器对象

# 迭代器对象
def ddq():
	print('ok')
	yield 1
	print('ok1')
	yield 2

d = ddq()# 这里是个迭代器对象,并不会执行
# a = next(d) #移动指针
# b = next(d)
# print(a,b) #1,2 yield返回的值
# for x in d: #d 就是自定义的生成器对象
# 	print(x)
# exit();

#斐波那契 数列
# def feibo(mx):
# 	n,b,a = 0,0,1
# 	while n<mx:
# 		print(b,a)
# 		b,a = a,b+a
# 		n= n+1
# print(feibo(10))
# exit()

# 改为跌对其对象
# def fib(mx):
# 	n,b,a = 0,0,1
# 	while n<mx:
# 		#print(b,a)
# 		yield a #就是每次迭代返回的值
# 		# yield [a,b] #就是每次迭代返回的值
# 		b,a = a,b+a
# 		n= n+1
# for x in fib(10):
# 	print(x)
# exit()

#迭代器 传值->send():next(b)和b.send()是一样的都是进入迭代器执行
def ddq1():
	print('ok')
	count = yield 1
	print('ok1',count)
	count = yield 2
	print('ok2',count)
	count = yield 3

d = ddq1()
# next(d)
s = d.send(None)#相当于next(d)
s1 = d.send('aaa') #调用send前必须使用next来进去生成器对象
s2 = d.send('bbbb')
print(s,s1,s2)
exit()

#什么是迭代器:
#满足两个条件,1,有iter方法 2,有next方法
#生成器与迭代器的关系:生成器满足 迭代器的两个协议
s = [1,2,3,4,5]
a = iter(s) #转换为可迭代对象
#c = a.send(None)
#print(c)
z = next(a)
print(z)
z = next(a)
print(z)
print(isinstance(a,list))#判断是否是个list
#print(isinstance(a,Iteration))#判断是否是个list



#时间戳
import time
#print(help(time))
print(time.time())
print(time.clock()) #计算cpu执行的时间
print(time.gmtime())#世界标准时间time.struct_time(tm_year=2017, tm_mon=9, tm_mday=2, tm_hour=10, tm_min=38, tm_sec=51, tm_wday=5, tm_yday=245, tm_isdst=0)
print(time.localtime())#本地时间time.struct_time(tm_year=2017, tm_mon=9, tm_mday=2, tm_hour=18, tm_min=40, tm_sec=1, tm_wday=5, tm_yday=245, tm_isdst=0)
print(time.strftime("%Y--%m--%d %H:%M:%S"))#2017--09--02 18:45:56
print(time.strptime('2017--09--02 18:45:56',"%Y--%m--%d %H:%M:%S"))#字符串日期 转换为元祖
a  = time.strptime('2017--09--02 18:45:56',"%Y--%m--%d %H:%M:%S");
print(a.tm_year)

print(time.ctime())#Sat Sep  2 18:53:14 2017
print(time.ctime(12392342300))#时间戳直接转换为时间Thu Sep 13 05:18:20 2362
print(time.mktime(time.localtime()))#将结构化事假转换为时间戳

import datetime #实际常用
#print(help(datetime)) #获取方法帮助
print(datetime.datetime.now())#2017-09-02 18:58:37.437710



#随机数
import random
#print(help(random))
print(random.random()) #0到1的随机数
print(random.randint(0,8))
print(random.choice('hello'))
print(random.choice(['qq','ww','rr']))
#print(random.shuffle(['qq','ww','rr']))
print(random.sample(['qq','ww','rr'],2))#随机选择几个元素
#print(random.choice({qq:'qq',ww:'ww',rr:'rr'}))#错误
print(random.randrange(1,6))

def ewm(num):
	code = ''
	for x in range(num):
		if x==random.randint(0,9):
			add = random.randint(0,9)
		add = chr(random.randrange(65,91)) #将数字转换为字母ASCII
		code+=str(add)
	return code
#print(ewm(5))

#改进版
def ewm1(num):
	code = ''
	for x in range(num):
		code += str(random.choice([random.randint(0,9),chr(random.randrange(65,91))]))
	return code
print(ewm1(5))