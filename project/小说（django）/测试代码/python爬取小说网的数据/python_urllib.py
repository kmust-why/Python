#encoding:utf-8
import re,urllib #从网页获取数据
import urllib.request
#import html.parser as h
import re

def getTypeList(pn=1):#用于获取分类列表的函数
    #实例化将要请求的对象  http://www.quanshuwang.com/map/1.html
    request = urllib.request.Request('http://www.quanshuwang.com/map/%s.html' %pn)
    request.headers = headers #替换所有头信息
    #request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    #decode是解码,解码成unicode码
    html = response.read().decode('gbk')
    #print(html)
    # <a href="1.html" class="hottext">玄幻魔法</a>
    reg =  '<a href="(.*?)" class="hottext">(.*?)</a>'
    reg = re.compile(reg)
    # 正则返回的是一个列表
    return re.findall(reg, html)

def getNovelList(url):
    request = urllib.request.Request(domain + url)
    #print(domain + url)
    request.headers = headers  # 替换所有头信息
    # request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    # decode是解码,解码成unicode码
    html = response.read().decode('gbk')  # 获取所有的源码
    #return html
    #<a href="/book/0/149/index.html" target="_blank">将夜</a>
    #reg = '<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    reg = '<a href="/(book/0/.*?/index.html)" target="_blank">(.*?)</a>'
    reg = re.compile(reg)
    # 正则返回的是一个列表
    return re.findall(reg, html)

def getChapterList(url):
    request = urllib.request.Request(domain + url)
    #print(domain + url)
    request.headers = headers  # 替换所有头信息
    # request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    # decode是解码,解码成unicode码
    html = response.read().decode('gbk')  # 获取所有的源码
    #return html
    #<li><a href="34333.html" title="开头">开头</a></li>
    reg = '<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    reg = re.compile(reg)
    # 正则返回的是一个列表
    return re.findall(reg, html)

def getNovelContent(url):
    request = urllib.request.Request(domain + url)
    #print(domain + url)
    request.headers = headers  # 替换所有头信息
    # request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    # decode是解码,解码成unicode码
    html = response.read().decode('gbk')  # 获取所有的源码
    #print(html)
    #reg = r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">style6\(\);</script>'
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\);'
    #reg = ' <li><a href="http://www.quanshuwang.com/list/(.*?)">(.*?)</a></li>'
    #reg = 'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    reg = re.compile(reg, re.S | re.M)
    # 正则返回的是一个列表
    return re.findall(reg, html)

#res = getNovelContent('book/0/742/238413.html')
#print(res)



domain = 'http://www.quanshuwang.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
if __name__ == '__main__':
    sort_list = getTypeList()
    #print(sort_list)
    for sort_url, sort_title in sort_list:
        print(domain + 'map/' + sort_url)
        type = int(sort_url.split('.')[0])
        novel_list = getNovelList('map/%s' %sort_url)
        for novel_url, novel_name in novel_list:
            if novel_name == '将夜':
                continue
            print(novel_url + novel_name)
            chapter_list = getChapterList(novel_url)

            for chapter_url, chapter_title in chapter_list:
                chapterid = int(chapter_url.split('.')[0])
                print(chapter_url, chapter_title)
                content_list = getNovelContent(novel_url.replace('index.html', chapter_url))
                for content in content_list:
                    print(content)





