print('metaclass')
class Mytype(type):
	def __init__(self, *args,**kwargs):
		print('Mytype')

	def __call__(self, *args,**kwargs):
		#调用self 的new方法
		obj = self.__new__(self, *args,**kwargs)
		self.__init__(obj)
		print('Mytype__call__')

		
class foo(object,metaclass=Mytype):
	def __init__(self, *args,**kwargs):
		print('__init__')

	def __new__(self, *args,**kwargs):
		print('创建对象__new__')
	    #return self.__new__(self, *args,**kwargs)
		
	def func(self):
	 	print('func')

########################################
# 上边这个类的本质(foo类 也是个对象)
# foo = type('foo',(object,),{'function':lambda x:123})
# obj = foo()
# print(obj.function())

#总结
#类 都是type类的对象

obj = foo()
#obj.func()


#异常处理
try:
	#li = [1,2,3,4]
	#li[100]
	# print('可能会出错的代码')
	# rest = DB()
	# if not rest:
	# 	raise Exception('数据库错误') #这里raise后后面的except Exception 会接收到这个错误信息
except IndexError, e:
	print('IndexError')
except ValueError, e:
	print('ValueError')
except Exception, e:
	print('Exception')
else:
	print('没有出错 执行这里')
finally:
	print('最后执行这里')


#自定义异常处理

class zdy(object):
	def __init__(self,msg):
		self.mesg = msg
		print('__init__')

	def __str__(self):
		return self.mesg

try:
	raise zdy('错误')
except Exception, e:
	print(e)

#断言
#assert 条件,强制用户服从,不服从就报错
print(23)
# 条件满足 才继续往下运行
assert 1==2
print(100)