print('oop')

class f1:
	static = '我是静态字段,属于类'
	def __init__(self):
		print('__init__')
	
	def func1(self):
		print(f1.static)#静态字段可以通过类获取,也可以通过对象获取
		print(self.static)

	@staticmethod
	def sta():
		print('static_fun,我是静态方法')

	@classmethod
	# 类方法有一个参数,是类名(当前类)
	def class_func(clssss):
		print('class_func---我是类方法')

	#成员属性
	@property
	def pro(self):
		return 'pro我被获取了'

	# 为属性设置值	
	@pro.setter
	def pro(self,val):
		print(val)

	#属性被删除的时候执行	
	@pro.deleter
	def pro(self):
		print('pro被删除了')

	# 属性的另外一种写法
	def f1(self):
		return 123

	def f2(self,val):
		print(val)

	def f2(self):	
		print('pro被删除了')
	pro = property(fget=f1,fset=f1,fdle=f3,doc='介绍')

obj = f1()
obj.func1()

#执行静态方法
f1.sta()

#执行类方法
f1.class_func()

#执行一个属性(将一个方法 通过property伪造为一个属性)
ret = obj.pro
print(ret)
obj.pro = 'pro被重新设置了'

# 删除pro 属性
del obj.pro
