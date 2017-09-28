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
#4、进行远程操作
stdin,stdout,stderr = ssh.exec_command('ls')
#说明ssh.exec_command会有三个返回值，
# 第一个代表要输入的内容，
#第二个代表执行命令之后返回的内容
#第三个代表如果执行错误，返回错误信息
#这三个参数返回的都是文件对象，需要对他们进行文件操作
#5、对返回的结果进行展示
with stdout as f:
    for i in f.readlines():
        print(i)

#6、关闭连接
ssh.close()

#上面的代码只能执行一条命令，无法实现对制定服务器连贯的操作。