print('反射')

class foo:
	start = 'wwwww'
	def __init__(self, name,age):
		self.name = name
		self.age = age


r = getattr(foo,'start')
setattr(foo,'key1','eeeee') #设置一个对象的属性
r = getattr(foo,'key1') #获取一个对象的属性
delattr(foo,'key1') #删除一个字段
#r = getattr(foo,'key1')
r = hasattr(foo,'key1') #对象是否 有这个字段
print(r)
