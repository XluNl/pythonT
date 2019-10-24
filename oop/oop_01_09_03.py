print('面向对象开始')
class Father:
	def __init__(self, arg):
		print(arg)

	def hejiu(self,name):
		print(name+"Father喝酒")

	def fff(self,name):
		print(name+'Father爸爸')

class Father1:
	def __init__(self, arg):
		print(arg)

	def hejiu(self,name):
		print(name+"Father1喝酒")
	
	def fff(self,name):
		print(name+'Father1爸爸')

#class demo(Father): 集成	
# 多继承的时候,子类会从左测优先
# 如果有同一个根,根最后执行
class demo(Father,Father1):
	#构造方法
	def __init__(self,host,port,ip):
		self.host = host
		self.port = port
		self.ip = ip
		print(self.host,self.port,self.ip)

	def foot(self,name):
		print(name)

	def booc(self,name):
		return name

	#重写父类的fff方法
	def fff(self,name):
		print(name+'儿子')

obj = demo('www.clp.com','3306','192.168.1.1')
obj.foot('clp')
obj.foot('xxx')
obj.foot('kkk')
print(obj.booc('2341235124'))

#继承
obj.hejiu('怕怕啪啪啪')
obj.fff('ccc')

