print('多继承')

class f2:
	def __init__(self):
		print('f1')

	def bb(self):
		print('bb_f2')

	def cc(self):
		print('cc_f2')
		# 注意这个self 代表obj,这里找bb这个方法会回到原点开始从左往右找
		# 所以调用的是f1里面的bb()
		self.bb()

class f1:
	def __init__(self):
		print('f1')	
	def ff(self):
		print('ff_f1')
	def bb(self):
		print('bb_f1')

class f3(f1,f2):
	def __init__(self):
		print('f3')

obj = f3()
obj.cc()