import paramiko

#1、创建一个ssh链接的实例
ssh = paramiko.SSHClient()
#2、制定当前ssh实例采用默认的受信列表，并且对不受信的计算机进行通过
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#3、远程登陆到指定的服务器
ssh.connect(
    hostname='172.93.39.34',#要连接的主机的ip
    port=29192,#端口
    username='root',#远程登陆的主机的用户名
    password='8W8XkW9sTM9h',#远程登陆的主机的用户名
)
#4、实例化一个shell
channel = ssh.invoke_shell()
#5、设置每条命令执行的超时时间
channel.settimeout(5)
#6、让shell执行该命令
channel.send(input('[root@localhost#]')+'\n')
#7、对shell返回的结果进行处理
while True:
    try:
        recv = channel.recv(9999)#接受shell返回的数据，每次最多接受9999个字节
        if recv:
            print(recv)
        else:
            continue
    except:
        command = input('[root@localhost#]')
        if command == 'break':
            channel.close()#关闭shell
            ssh.close() #关闭ssh
        else:
            channel.send(command+'\n')