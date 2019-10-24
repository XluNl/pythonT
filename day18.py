import os
print('2017-9-2')

print(os.getcwd())
print(os.curdir)
print(os.pardir)
#os.makedirs('abc\\ccc') #生成多个文件夹
#os.removedirs('abc\\ccc')#只能删除空文件夹
#os.mkdir(r'.\vvvv')
print(__file__) #E:\python_text\day18.py
print(os.path.dirname(__file__))#E:\python_text
# print(os.path.join(['www','ccc'])) #将两个路径拼接

#系统模块
import sys
print(sys.path)
#['E:\\python_text', 'D:\\Program Files\\python35.zip', 'D:\\Program Files\\DLLs', 'D:\\Program Files\\lib',
#'D:\\Program Files', 'D:\\Program Files\\lib\\site-packages']
# 在控制台里面 执行这个脚本文件时可以传值
#C:\Users\clp>python E:\python_text\day18.py path ppp
print(sys.argv) #['E:\\python_text\\day18.py', 'path', 'ppp']
# if sys.argv[1]=='path':
# 	print('上传文件')

# 获取平台
print(sys.platform) #win32



#hashlib
import hashlib  #加密(MD5)

#m = hashlib.md5()
#print(m)
#m.update('hello world'.encode('utf8'))
#print(m.hexdigest())#5eb63bbbe01eeed093cb22bb8f5acdc3

m = hashlib.md5()
#1
m.update('hello world'.encode('utf8'))
print(m.hexdigest())#5eb63bbbe01eeed093cb22bb8f5acdc3
#2 相当于'hello worldclp'
m.update('clp'.encode('utf8'))
print(m.hexdigest())#1018492249534b07cbbd86c937c7e6e0
#3 这一步是为了验证第二步
m.update('hello worldclp'.encode('utf8'))
print(m.hexdigest())#1018492249534b07cbbd86c937c7e6e0
# 3 = 2+1

#sha1
sha = hashlib.sha256()
#sha = hashlib.sha1()
#sha = hashlib.sha512()
sha.update('hello world'.encode('utf8'))
print(sha.hexdigest())
#sha256->64位:b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
#sha1->40位:2aae6c35c94fcfb415dbe95f408b9ce91ee846ed


#logging Model
import logging
#print(help(logging))
print(logging.debug('debug message'))
print(logging.info('info message'))
print(logging.warning('warning message'))#警告
print(logging.error('error message'))#错误
print(logging.critical('critical message')) #严重的 致命的