#coding:utf-8
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
        #print(url_name)
    for i in url_name:#i[0]name i[1]url
        print(i[0])
        print(i[1])
        urllib.request.urlretrieve(i[1],'视频\\%s.mp4' %(i[0]))
    return text

get()


