#coding:utf-8
#1.导入socket模块
import socket

#2.实例化一个和要连接的服务器端对应的socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#3.连接服务端,这里写的是服务端的Ip和对应的端口
print('客户端运行中...')
sock.connect(('127.0.0.1',8012))
#4.进行信息的发送和接收
while True:
    sends = input('客户端输入信息:').encode(encoding='utf-8', errors = 'strict')
    sock.send(sends)
    reces = sock.recv(512).decode('UTF-8')
    print(reces)
#5.关闭套接字
sock.close()
