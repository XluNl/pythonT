print('client')

# 文件上传
import socket
import os
import urllib.parse

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.connect(address)

bas_dir= os.path.dirname(os.path.abspath(__file__))
print(bas_dir)
while True:
	inpot = input('>>>').strip()
	if inpot=='exit':break
	cmd,path = inpot.split('|')

	#上传文件的绝对路径
	path = os.path.join(bas_dir,path)
	print(path)
	# 文件名(从一个路径获取文件名)
	(base_name,file_name) = os.path.split(path) #python 不支持此方法

	# 根据文件绝对路径获取文件大小
	filesize = os.stat(path).st_size
	print(filesize)
	#打包数据,一起发送
	fileinfo = 'post|%s|%s'%(file_name,filesize)
	print(fileinfo)
	#发送数据
	sk.sendall(bytes(fileinfo,'utf8'))
	#发一次数据 就等待服务器应答,避免粘包(这里阻塞着等待服务器回应，如果没有回应则一直阻塞)
	# data = sk.recv(1024)
	# print(str(data,'utf8'))
	#打开一个文件(以byte读写),发送
	has_byte = 0
	with open(path,'rb') as f:
		# 不停发送
		while has_byte != filesize:
			da = f.read(1024)
			sk.sendall(da)
			has_byte+=len(da)
	f.close()
	
sk.close()