#coding:utf-8
#1.导入socket模块
import socket

#2.实例化一个socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#注意其中的两个参数family,type
#family分为:
#AF_INET,适合ipv4类型的数据传输
#AF_INET6,适合ipv6类型的数据传输
#AF_UNIX,适合Unix类型的数据传输

#type分为：
#SOCK_STREAM TCP协议
#SOCK_DGRAM UDP协议
#3.绑定Ip,指的是将socket套接字绑定到自己的Ip上

#绑定需要一个双元素的元组，(ip,port)
#其中ip如果为空，代表给自己网卡所有IP绑定该套接字
#其中port表示信息传输占用的端口，端口可以是任意一个没有被使用
#65535 通常使用的是1000以上的端口
sock.bind(('127.0.0.1',8012))
#4.监听,设置监听队列的长度
sock.listen(5)
#5.进行消息的接收和发送
#这个方法返回两个参数
#第二个参数代表客户端的IP和端口
#第一个参数代表接收和发送消息的功能
print('服务器运行中...')
con,add = sock.accept()
print('%s is connected'%add[0])
#6.进行消息的发送和接收
while True:
    reces = con.recv(512).decode('UTF-8')
    print(reces) #这个就是具体的接收消息，需要指定每次接受的字节数
    sends = input('服务器输入信息:').encode(encoding='utf-8', errors = 'strict')
    con.send(sends) #发送消息
#7.关闭套接字
sock.close()
