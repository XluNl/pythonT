print('类的特殊成员')

class foo:
	def __init__(self,name,age):
		self.name = name
		self.age  = age
		print('__init__')

	# 特殊成员
	def __call__(self,*args,**kwargs):
		print('__call__')

	#对象被转换为int的时候 调用__int__
	def __int__(self):
		return 123

	#对象被转换为str的时候,被打印的时候 调用__str__
	def __str__(self):
		return '__str__'

	#对象被销毁的时候执行
	def __del__(self):
		return '__del__'

	# 两个对象相加的时候(self代表第一个相加的第一个对象,other代表第二个对象)
	def __add__(self,other):
		return self.number+other.number

	#将对象里面的成员 已字典的形式返回
	# def __dict__(self):
	# 	print('__dict__')

	def __getitem__(self,item):
		if type(item)==slice:
			print(item.start)
			print(item.stop)
			print(item.step)
			print('我是个 slice')
		else:
			print(item+20)

	def __setitem__(self,key,value):
		print(key,value)

	def __delitem__(self,key):
		print(key)

	# 对象遍历
	def __iter__(self):
		# 返回的是一个迭代器
		return iter([11,22,33])


obj = foo('clp',28)
obj.number = 10
#对象加括号 调用的是 __call__方法
obj()
print(obj)
#__dict__ 会把对象的成员属性 已字典的形式返回
print(obj.__dict__)

# 使用对象的迭代器
for x in obj:
	print(x) #输出11 22 33

# 调用__getitem__,__setitem__,__delitem__
obj[123] #__getitem__
obj[123] = 400 #__setitem__
#obj[1:4:2]
del obj[123] #__delitem__

#两个对象相加,可以自定义对象相加的方法
obj1= foo('clp',28)
obj1.number = 20
obj2 = obj+obj1
print(obj2) #输出30