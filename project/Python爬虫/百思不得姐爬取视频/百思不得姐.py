#coding:utf-8
from tkinter import *
from tkinter import scrolledtext # 导入滚动文本框的模块
import threading
import requests
import re
import urllib
import urllib.request

url_name = [] #用来放url+name
#1、获取主页源码
def get():
    url = 'http://www.budejie.com/video/'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}

    request = requests.get(url=url, headers=header)
    text = request.content.decode('UTF-8')  # 获取所有的源码
    #print(text)
    url_content = re.compile('<div class="j-r-list-c">.*?</div>.*?</div>',re.S) #编译提高效率
    url_contents = re.findall(url_content,text)
    for i in url_contents:#代表了大盒子里面的源码
        #匹配视频
        url_reg = 'data-mp4="(.*?)"' #视频地址
        url_items = re.findall(url_reg,i)
        if url_items:#判断视频存不存在
            name_reg = re.compile('<a href="/detail-.{8}?.html">(.*?)</a>',re.S)
            name_items = re.findall(name_reg,i)
            #print(name_items[0])
            for i,k in zip(name_items,url_items):
                #print(i,k)
                url_name.append([i,k])

id = 1
def write():
    #print('按钮被按下了')
    global id
    while id < 10:
        get()
        for i in url_name:
            urllib.request.urlretrieve(i[1], '视频\\%s.mp4' % (i[0]))
            text.insert(END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')
            url_name.pop(0)
            id += 1
    var1.set('蘑菇头：视频链接和视频捉去完毕！over.')
def start():
    th = threading.Thread(target=write)
    th.start()


root = Tk() #root代表窗口
root.title('python界面')
text = scrolledtext.ScrolledText(root,font=('微软雅黑',10))
text.grid() #grid布局
button = Button(root,text='开始爬取',font=('微软雅黑',10),command=start) #绑定函数
button.grid()
var1 = StringVar()#变量
label = Label(root,font=('微软雅黑',10),fg='red',textvariable=var1)
label.grid()
var1.set('熊猫已准备...')

root.mainloop() #用于创建窗口的命令