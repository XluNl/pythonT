print('day14 function---深浅拷贝')

import copy
# 浅copy 只copy一层买其他(2,3)层都是共享
# a = [[1,2],'2342','34545']
# print(a)
# b = a.copy() #浅拷贝 只拷贝一层
# #b = a.deepcopy() #深拷贝,完全拷贝一份
# b[0][1] = 4444
# print(a)
# print(b)

#set集合(可别,不可变),特点(集合里面的值不能够重复)
# s = set('cjenlipen')
# print(s) #{'j', 'c', 'p', 'l', 'n', 'i', 'e'}
# s1 = ['sdds',243,'dfsdfd']
# s2 = set(s1)
# s2.add('55555') #添加
# s2.update('wdfg')
# s2.update([8,8,9]) #添加多个元素
# s2.pop() #随机删
# #print(s2,type(s2)) #{'dfsdfd', 'sdds', 243} <class 'set'>
# s2 = list(s2) #set转list
# #print(s2,type(s2)) #['dfsdfd', 243, 'sdds'] <class 'list'>

#print(set('clp')<set('clppw')) #true,第二个包含第一个
# or 取交集
#print(set('clp') or set('clppw')) #{'p', 'l', 'c'}
# and 取联合
#print(set('clp') and set('clppw')) #{'p', 'w', 'l', 'c'}

#注意
#s3 = [[1,2],3,4]
#s4 = set(s3) 
#print(s4) #TypeError: unhashable type: 'list'(set集合里面不能包含可哈希数据类型)


#**kwargs 接收带名字的参数,必须在右边;*args接收无名参数,必须在左边;sex与agrs是同级的
#参数优先级:func(name,name='clp',*args,**kwargs)
# def function(sex='rrrrr',*args,**kwargs):
# 	print(args)
# 	print(kwargs)
# 	print(sex)
#
# function('bbbbb',2,3,name=5,age=6)
# exit()

# 函数返回值
# def add(a,b):
# 	return a+b
# print(add(1,3))

#注意 作用域
# count = 10
# def ff():
# 	# global count #声明为全局变量
# 	#nonlocal count
# 	print(count) #local variable 'count' referenced before assignment
# 	count = 5 #(方法在内存里面已经找到了count)报错意思是 得在调用前声明count
# ff()
# exit()

#函数作为参数
# def a(a):
# 	return a*a
# def foo(a,b,func):
# 	return func(a) + func(b)
# print(foo(2,2,a))
# exit()

#函数作为返回值
# def lazy_sum(*args):
#     def sum():
#         x=0
#         for n in args:
#         	x = x + n
#         return x
#     return sum #注意这里返回的sum是个函数名,并没有调用sum()
#
# la = lazy_sum(1,2,3,4,5)
# print(la())#调用函数
# exit()

#阶乘
#5*4*3*2*1
# def fcet1(n):
# 	res = 1
# 	for x in range(1,n+1):
# 		res = res*x
# 	return res
# print(fcet1(500))#普通版
# exit()
		
def fcet(n):
	print(n)
	if n==1:
		return 1
	ret = n*fcet(n-1)
	print(n,ret)
	return ret
print(fcet(5))#改进版