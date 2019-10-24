print('server')

import socket
import os

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)
print('wating..............')

bas_dir= os.path.dirname(os.path.abspath(__file__))
print(bas_dir)

while 1:
	conn,addr = sk.accept()
	print(conn)
	while 1:
		try:
		# 服务端阻塞在这里,等到回复,如果客户端强行退出 则会出错
			data = conn.recv(1024)
			print(data)
			cmd,filename,filesize = str(data,'utf8').split('|')
			path = os.path.join(bas_dir,'img',filename)
			filesize = int(filesize)
			# conn.send(bytes('接收头','utf8'))
			print(path)
			print(filesize)
			# 打开一个文件,将数据往往进装(以字节的方式往里写)
			f = open(path,'ab')
			print(f)
			has_byte = 0
			# 循环不停接收
			while has_byte != filesize:
				print('start_rec')
				data = conn.recv(1024)
				print(data)
				f.write(data)
				has_byte += len(data)
			f.close()
		except Exception as e:
			break			
		if not data:break
		# 回复
		inpot = input('>>>')
		conn.send(bytes(inpot,'utf8'))
sk.close()
print('sk.close')