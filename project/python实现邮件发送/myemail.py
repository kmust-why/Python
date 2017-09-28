import smtplib #发送模块
#from email import MIMEText
from email.mime.text import MIMEText

msg = MIMEText('hello world,send by Python...','plain','utf-8') #正文
msg['Subject'] = 'Python test' #主题
msg['From'] = '1563713769@qq.com' #发件人邮箱
msg['To'] = '1981175183@qq.com' #收件人邮箱

server = smtplib.SMTP_SSL('smtp.qq.com',465) #邮件服务器
server.set_debuglevel(1)
server.login('1563713769@qq.com','axrfzmsvakkwjhjc')
Tolist = ['1981175183@qq.com',]
server.sendmail('1563713769@qq.com',Tolist,msg.as_string())
server.quit()