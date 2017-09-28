#encoding:utf-8
import re,urllib #从网页获取数据
import urllib.request
#import html.parser as h
import re

import psycopg2

def connectPostgreSQL():
    conn = psycopg2.connect(database="testdb", user="postgres", password="123456", host="127.0.0.1", port="5432")
    # print 'connect successful!'
    cursor = conn.cursor()
    cursor.execute('''create table public.member(
id integer not null primary key,
name varchar(32) not null,
password varchar(32) not null,
singal varchar(128)
)''')
    conn.commit()
    cursor.close()
    conn.close()
    print('table public.member is created!')

def insertOperate(sql):
    conn = psycopg2.connect(database="novel", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

    print('insert records successfully')

def selectOperate(sql):
    conn = psycopg2.connect(database="novel", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        #print('id=', row[0], ',name=', row[1], ',pwd=', row[2], ',singal=', row[3], '\n')
        mynovelid = row[0]
    cursor.close()
    conn.close()
    return mynovelid

def updateOperate():
    conn = psycopg2.connect(database="testdb", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cursor=conn.cursor()
    cursor.execute("update public.member set name='update ...' where id=2")
    conn.commit()
    print("Total number of rows updated :", cursor.rowcount)

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
    cursor.close()
    conn.close()

def deleteOperate():
    conn = psycopg2.connect(database="testdb", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cursor=conn.cursor()

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')

    print('begin delete')
    cursor.execute("delete from public.member where id=2")
    conn.commit()
    print('end delete')
    print("Total number of rows deleted :", cursor.rowcount)

    cursor.execute("select id,name,password,singal from public.member")
    rows=cursor.fetchall()
    for row in rows:
        print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
    cursor.close()
    conn.close()




def getTypeList(pn=1):#用于获取分类列表的函数
    #实例化将要请求的对象  http://www.quanshuwang.com/map/1.html
    request = urllib.request.Request('http://www.quanshuwang.com/map/%s.html' %pn)
    request.headers = headers #替换所有头信息
    #request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    #decode是解码,解码成unicode码
    html = response.read().decode('gbk', 'ignore')
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
    html = response.read().decode('gbk', 'ignore')  # 获取所有的源码
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
    html = response.read().decode('gbk', 'ignore')  # 获取所有的源码
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
    html = response.read().decode('gbk', 'ignore')  # 获取所有的源码
    #print(html)
    #reg = r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">style6\(\);</script>'
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\);'
    #reg = ' <li><a href="http://www.quanshuwang.com/list/(.*?)">(.*?)</a></li>'
    #reg = 'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    reg = re.compile(reg, re.S | re.M)
    # 正则返回的是一个列表
    return re.findall(reg, html)



domain = 'http://www.quanshuwang.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
if __name__ == '__main__':
    sort_list = getTypeList()
    #print(sort_list)
    for sort_url, sort_title in sort_list:
        print(domain + 'map/' + sort_url)
        type = int(sort_url.split('.')[0])
        if type == 1:
            continue
        novel_list = getNovelList('map/%s' %sort_url)
        for novel_url, novel_name in novel_list:
            if novel_name == '将夜':
                continue
            print(novel_url + novel_name)
            sql = "insert into public.novel(type,novelname) values('%s', '%s')" %(sort_title, novel_name)
            insertOperate(sql)
            sql = "select novelid from public.novel where novelname='%s'" %novel_name
            mynovelid = selectOperate(sql)
            chapter_list = getChapterList(novel_url)

            for chapter_url, chapter_title in chapter_list:
                #chapterid = int(chapter_url.split('.')[0])
                print(chapter_url, chapter_title)
                content_list = getNovelContent(novel_url.replace('index.html', chapter_url))
                for content in content_list:
                    sql = "insert into public.chapter(title, content, novelid) values('%s', '%s', %d)" %(chapter_title, content, mynovelid)
                    insertOperate(sql)
                    #print(content)




