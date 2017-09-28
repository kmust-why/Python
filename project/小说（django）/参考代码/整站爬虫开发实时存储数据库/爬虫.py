#encoding:utf-8
import re,urllib #从网页获取数据
import urllib.request
import html.parser as h
import re
import pymysql as sql

class Sql(object):
    conn = sql.Connect(
        host='localhost',  # 表示指定连接数据库的服务器的名称，可以使用主机名，也可以是ip
        user='root',  # 数据库的用户，注意如果远程登录数据库，默认不可以用root
        passwd='123456',  # 对应数据库用户的密码
        # port = '3306',#数据库的端口，默认为3306,该参数在python3中已经没有了
        db='xs'  # 指定要操作的数据库的名称
    )
    #conn.set_character_set('utf8')
    conn.character_set_name()
    #conn.encoding('utf-8')
    def addNovels(self,sort,novelname):
        cur = self.conn.cursor()

        #cur.execute("insert into novel(sort,novelname) values(%d,%s)" %(sort,novelname))
        sqls = "insert into novel(sort,novelname) values(1,'why')"
        cur.execute(sqls)
        lastrowid = cur.lastrowid
        cur.close()
        self.conn.commit()
        return lastrowid
    def addChapters(self,novelid,chaptername,content):
        cur = self.conn.cursor()
        #"insert into chapter(novelid,chaptername,content) values(%d,%s,%s)" % (novelid, chaptername, content)
        sqls = "insert into chapter(novelid,chaptername,content) values(%d,%s,%s)" %(novelid,chaptername,content)
        cur.execute(sqls)
        cur.close()
        self.conn.commit()
domain = 'http://www.quanshu.net'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
def getTypeList(pn=1):#用于获取分类列表的函数
    #实例化将要请求的对象
    request = urllib.request.Request('http://www.quanshu.net/map/%s.html' %pn)
    request.headers = headers #替换所有头信息
    #request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    #decode是解码,解码成unicode码
    html = response.read().decode('gbk','ignore')  # 获取所有的源码
    print(html)
    reg = '<a href="(/book/.*?)" target="_blank">(.*?)</a>'
    reg = re.compile(reg)
    #正则返回的是一个列表
    return re.findall(reg,html)

def getNovelList(url):
    request = urllib.request.Request(domain + url)
    request.headers = headers  # 替换所有头信息
    # request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    # decode是解码,解码成unicode码
    html = response.read().decode('gbk','ignore')  # 获取所有的源码
    #return html
    reg = '<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    reg = re.compile(reg)
    # 正则返回的是一个列表
    return re.findall(reg, html)

def getNovelContent(url):
    # 实例化将要请求的对象
    request = urllib.request.Request(domain + url)
    request.headers = headers  # 替换所有头信息
    # request.add_header() #添加单个头信息
    response = urllib.request.urlopen(request)  # 开始请求
    # decode是解码,解码成unicode码
    html = response.read().decode('gbk','ignore')  # 获取所有的源码

    reg = 'style5\(\);</script>(.*?)<script type="text/javascript">style6\(\)'
    reg = re.compile(reg)
    # 正则返回的是一个列表
    return re.findall(reg, html)[0]

mysql = Sql()
'''
if __name__ == '__main__':
    for sort in range(1,10):
        for url,title in getTypeList(sort):
            #lastrowid = mysql.addNovels(sort,title)
            #lastrowid = mysql.addNovels(sort,title)
            #print(type(sort),type(title))
            for zurl,ztitle in getNovelList(url):

                #print(zurl,ztitle)
                print('正在爬取----%s' %ztitle)
                content = getNovelContent(url.replace('index.html',zurl))
                print('正在存储----%s' %ztitle)
                #mysql.addChapters(novelid=lastrowid,chaptername=ztitle,content=content)
            break
        break
'''


getTypeList(1)