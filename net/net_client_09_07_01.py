print('client')

import socket
sk = socket.socket()
address = ('127.0.0.1',8000)
sk.connect(address)
while True:
	inpot = input('>>>')
	# 如果发送
	if inpot=='exit':break
	sk.send(bytes(inpot,'utf8'))	
	data = sk.recv(1024)
	print(str(data,'utf8'))

sk.close()