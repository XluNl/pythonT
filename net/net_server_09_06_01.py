print('net_server')

import socket
#创建一个监听服务
sk  = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3) 
print('wating.......等待客户端连接')
conn,addr= sk.accept()
#(<socket.socket fd=356, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 35652)>, ('127.0.0.1', 35652))
# 3.0以前可以直接字符串,以后需要使用byte类型
# 服务端的 conn给客户端发送数据
conn.send(bytes('cilent_你好','utf8'))

# server 接收数据
data = conn.recv(1024)
print(str(data,'utf8'))
#conn.send(bytes('哈哈哈','utf8'))
# 发送
#sk.sendall(conn)
#关闭一个连接
conn.close()
# 关闭监听服务
sk.close()

