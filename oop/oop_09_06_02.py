print('单例')

class foo:
	start = 'wwwww'
	__v = None
	# def __init__(self, name,age):
	# 	self.name = name
	# 	self.age = age

	@classmethod
	def get_inst(cls):
		if not cls.__v:
			cls.__v = foo()
			return cls.__v
		else:
			return cls.__v

		
# 地址都是一样的
obj = foo.get_inst()
print(obj)
obj1 = foo.get_inst()
print(obj1)