print('server')

import socket
sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)
print('wating..............')
#conn,addr = sk.accept()
# while True:
# 	# 接收,这里只有接收有值才会往下走,不然一直阻塞,知道接收到数据
# 	try:
# 		# 服务端阻塞在这里,等到回复,如果客户端强行退出 则会出错
# 		data = conn.recv(1024)
# 		print(str(data,'utf8'))
# 	except Exception as e:
# 		conn.close()
# 		conn,addr = sk.accept()	
	
# 	if not data:
# 		conn.close()
# 		conn,addr = sk.accept()	
# 	# 回复
# 	inpot = input('>>>')
# 	conn.send(bytes(inpot,'utf8'))

# sk.close()

while 1:
	conn,addr = sk.accept()	
	while 1:
		try:
		# 服务端阻塞在这里,等到回复,如果客户端强行退出 则会出错
			data = conn.recv(1024)
			print(str(data,'utf8'))
		except Exception as e:
			break			
		if not data:break
		# 回复
		inpot = input('>>>')
		conn.send(bytes(inpot,'utf8'))
sk.close()