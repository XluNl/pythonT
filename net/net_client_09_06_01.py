print('net_client')

import socket
sk  = socket.socket()
address = ('127.0.0.1',8000)
sk.connect(address)

# 阻塞 等待接收数据
strr = sk.recv(1024) 
# 如果接受的是汉字,是bytes 则需要转换为utf8 直接转换为str
print(str(strr,'utf8'))

sk.send(bytes('server_你好','utf8'))