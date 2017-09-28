#encoding:UTF-8
import re,urllib #从网页获取数据
import urllib.request
import html.parser as h

url = 'http://daily.zhihu.com/'


def characterProcessing(html):
    #htmlParser = HTMLParser.HTMLParser()
    pattern = re.compile('<p>(.*?)</p>|<li>(.*?)</li>.*?', re.S)
    items = re.findall(pattern, html)
    result = []
    for index in items:

        if index != '':
            for content in index:
                tag = re.search('<.*?>', content)
                http = re.search('<.*?http.*?', content)
                html_tag = re.search('&', content)
                if html_tag:
                    content = h.unescape(content)

                if http:
                    continue
                elif tag:

                    pattern = re.compile('(.*?)<.*?>(.*?)</.*?>(.*)')
                    items = re.findall(pattern, content)
                    content_tags = ''
                    if len(items) > 0:
                        for item in items:
                            if len(item) > 0:
                                for item_s in item:
                                    content_tags = content_tags + item_s
                            else:
                                content_tags = content_tags + item_s
                        content_tags = re.sub('<.*?>', '', content_tags)
                        result.append(content_tags)
                    else:
                        continue
                else:
                    result.append(content)
    return result

#1.获取主页的源码
def getHtml(url):
   #header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
   #request = urllib.request(url) #用地址创建一个request对象
   response = urllib.request.urlopen(url) #打开网址
   text = response.read().decode('UTF-8')#获取所有的源码
   #print(text)
   return text

#2.解析每条日报的链接
def getUrls():
    pattern = re.compile('<a href="/story/(.*?)"',re.S)#正则表达式,其中的(.*?)表示匹配任意字符，re.S匹配换行符
    items = re.findall(pattern,html)
    #print(items)
    urls = []
    for item in items:
        urls.append('http://daily.zhihu.com/story/'+item)
        #print(urls[-1])
    return urls

#3.获取日报的内容
def getContent(url):
    html = getHtml(url)
    pattern = re.compile('<h1 class="headline-title">(.*?)</h1>')
    items = re.findall(pattern,html)
    #获取日报标题
    print('**********'+items[0]+'**********')
    #获取日报正文内容
    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        for content in characterProcessing(item):
            print(content)


if __name__  == '__main__':
    html = getHtml(url)
    urls = getUrls()
    for url in urls:
        try:
            getContent(url)
        except Exception as e:
            print(e)
