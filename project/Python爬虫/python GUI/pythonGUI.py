#coding:utf-8
from tkinter import *
from tkinter import Message
from PIL import Image
import requests
import re
import urllib
import urllib.request

def getImg():
    name = 'why'
    url = 'http://www.uustv.com/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}

    request = requests.get(url=url, headers=header,data='word:%s&sizes:60&fonts:jfcs.ttf&fontcolor:#000000' %name)
    #request = requests.get(url=url, headers=header)
    text = request.content.decode('UTF-8')  # 获取所有的源码
    #return text
    #匹配到图片
    reg = '<div class="tu"><img src="(.*/)" /></div>'
    #imgurl = 'http://www.uustv.com/'
    url_items = re.findall(reg,text,re.S)
    print(url_items)


def start():
    #print('ddd')
    #text = getImg()
    #print(text)
    getImg()

root = Tk() #root代表窗口
root.title('python签名设计')
root.geometry('320x120+400+300') #设置窗口的大小
label = Label(root,text='姓名:',font =('华文新魏',20),fg='red')
label.grid() #grid布局
entry = Entry(root,font =('华文新魏',20),fg='blue')
#entry.grid(row=0,column=1) #设置位置，row表示设置行数，column表示设置列数，从0开始计算。
entry.grid()
button = Button(root,text='一键生成签名',font=('华文新魏',20),width='15',height='1',command=start) #绑定函数
button.grid() #可以对该控件设置大小

root.mainloop() #用于创建窗口的命令
