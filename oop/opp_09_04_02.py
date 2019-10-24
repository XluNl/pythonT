print('成员修饰符')

class foo:
	def __init__(self,name,age):
		print('__init__')
		self.name = name
		# 代表私有属性
		self.__age= age

	# 外部间接访问私有属性
	def getage(self):
		return self.__age

	# 静态方法
	def __func1(self):
		return 12

	# 外部间接访问 私有方法
	def get_func1(self):
		return self.__func1()


obj = foo('clp',28)
print(obj.name)
#print(obj.age) #出错,无法访问
print(obj.getage())

# 调用私有方法出错
#print(obj.func1)
print(obj.get_func1())

class fat:
	def __init__(self, arg):
		self.pre = 123
		self.__prec = 456
		self.__agg = arg

class fat1(fat):
	def __init__(self):
		# 子类执行父类的构造方法
		super(fat1, self).__init__('hhhhhh')
		
		self.name = 'clp'
		self.__age = 28

	def show(self):
		print(self.name) #没问题
		print(self.__age) #访问自己的私有属性 也没问题
		print(self.pre) #访问父类的普通成员 没有问题
		#AttributeError: 'fat1' object has no attribute '_fat1__prec'
		print(self.__prec) #访问父类的私有属性,会出错,也证明了当前类只能呢过访问自身类的私有属性

obj = fat1()
obj.show()



