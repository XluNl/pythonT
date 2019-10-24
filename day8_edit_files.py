import os
print('day-8------文件操作')

# 打开文件的模式有三种(r->读取,w->写,a->追加),文件不存在会创建这个文件
#f  = open('data.txt','r') #FileNotFoundError: [Errno 2] No such file or directory: 'data.txt' 
#f  = open('E:\python_text\data1.txt','w',encoding='utf-8') #正确
#f.write('hello world \n')
#f.write('陈立鹏\n')
#f.write('东风工地上干第三个\n')
#f.write('分公司等公司东风公司打工\n')
#data = f.read()

# 读取
f  = open('E:\python_text\data1.txt','r',encoding='utf-8') #正确
#data = f.read(3)# 读取字符长度
#data = f.readline()
#print(f.readline()) #每读一行,指针就移到行尾
#print(f.readline())

#方法1
#print(f.readlines()) #变为一个列表,每一行为一个元素
#for x in f.readlines():
#	print(x.strip()) #strip() 取出字符传两端的空格及(换行符)

# 简便方法(for循环 会吧f作为一个迭代器,用一行取一行)
for x in f:
	print(x.strip())
f.truncate(5)#a模式的时候保留5个字符,w,r模式没有意义 其他全部删掉
f.close() #关闭文件 并且将缓存区的数据写入到文件

#缓存刷新
import sys,time
#for x in range(30):
#	sys.stdout.write('*') #sys.stdout,也是一个文件句柄
#	sys.stdout.flush() #实时将内存的数据 推到前台
#	time.sleep(0.2)
	#print('*')
# 缓存刷新 简便方法
for x in range(30):
	print('*',end='',flush=True)
	time.sleep(0.2)

#with 打开文件的方式(会自动 帮助关闭文件->close)
with open('path','w') as f:
	f.write('353432')
	f.write('4123424')

#with 同时操作多个文件
with open('path','w') as f,open('path1','r') as f1:
	f.write('2421342')
	f1.read()
#注意
#r:读  r+:读写(追加到最后) a:追加 a+:从最后追加 w:写 w+:格式化清空,再写
#f.seek(0);调整光标位置
#f.tell();查看光标位置
# 修改某一行内容,方案,直接在某一行的时候使用wirte是错误的,因为文件的写入机制是从最后开始
# 解决方案,重新建一个文件,将源文件的内容一行一行搬到新文件