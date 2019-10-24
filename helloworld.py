
#print("hello world")
# name = "clp"
# age = 12
# print('wewqew'+str(age)+name+"234124124");

# name = input("your name=");
# age = input("your age=");
# print(name,age);

# if 2==2:
#     print("相等等");
# else:
#     print("not xd");

#遍历
# for x in range(1,10,2):
# 	print(x)
# 	break #如果for 没有执行完毕  则不会执行else,此语法为python独有(for,where,)
# else:
# 	print('cansel')


#列表
a = [5,3,1]
b = [7,4,2]
c = a+b
print(c)
#d = c.sort() // 没有像我们预想的一样 会返回一个排序后的列表
c.sort(reverse=True)  #reverse=True 降序 默认fales升序
print(c)

a = ['a','b','c']
b = ['s','m','n']
c = a+b
print(c)
c.sort()
print(c)

#元祖(不希望被修改的数据)
print("/////////////////////////////////////////////////////////")
# a = ()
# a = (12,13,15,16)
# print(a[1:2])

# a,b = [1,2]
# print(a)
# print(b)
# a,b = [1,2],[3,4,5]
# print(a)
# print(b)

#判断输入的是否是一个数字
# a = input("请输入")
# if a.isdigit():
# 	print('是数字')
# else :
# 	print('不是数字')

#dic(字典)
dic = {"name":[1,2,3],"age":"26"}

dic.setdefault('sg','170') #key 存在则不添加，返回对应的值，不存在则添加
print(dic)
print(dic['name'][2])
print(dic.keys())
lis = list(dic.keys()) #转为list
for x in dic.keys(): #也可以直接便利
	#print(x)
	print(dic[x])
#for x in dic:
	#print(dic[x])

dic1 = {'text':'cc','123':'www'}
dic.update(dic1) #将一个字典的元素 全部加入到另外一个字典中
print(dic)

# dic.clear()  #清空字典
# print(dic)

# dic.pop('name') #删除一个元素
# print(dic)

# dic.popitem()  #随机删除一组元素
# print(dic)

# dic2 = dict.fromkeys(['ww','bb','cc'],'text') #创建个字典，值都为text
# print(dic2) #{'bb': 'text', 'cc': 'text', 'ww': 'text'}
# dic2 = dict.fromkeys(['ww','bb','cc'],[1,2]) #创建个字典，值都为[1,2]
# print(dic2) #{'ww': [1, 2], 'cc': [1, 2], 'bb': [1, 2]}

# dic3 = {5:'666',1:'444',3:'555'}
# print(sorted(dic3.items())) #按照索引（key）排序
# print(sorted(dic3.values())) #按照值做排序

#字符串
print("/////////////////////////////////////////////////////////")
a = 'qqq'
b = 'bbb'
c = 'ccc'
print(a,b,c) #qqq bbb ccc
d = ''.join([a,b,c]) #拼接字符串建议使用join
print(d) #qqqbbbccc
d = '------'.join([a,b,c]) #拼接字符串建议使用joi
print(d) #qqq------bbb------ccc

a = 'fsfsafgsdgdg {name} and {age}'
#a.index('s') #查找位置
#a.find('s')  #和index 一样
print(a.format_map({'name':'clp','age':28})) #fsfsafgsdgdg vlp and 28
aa = a.format_map({'name':'clp','age':28})  #会啊返回一个拼接后的字符串
print(aa)
aa = a.format(name="vlp",age=28)  #和format_map 是一样的功能 
print(aa)




