import requests
import re
from urllib import request


#获取源代码
#获取视频
"""
res = requests.get('http://www.budejie.com/video/')
html = res.content.decode('utf-8')
#print(html)
reg = r'data-mp4="(.*?)"'#r表示当前的字符串不会被转义，是原始的字符串
url_list = re.findall(reg,html)#正则匹配的返回值为列表
#print(url_list)
for url in url_list:
    print(url)
    request.urlretrieve(url,'../video/%s' %(url.split('/')[-1]))

"""


#获取图片
res = requests.get('http://www.budejie.com/pic/')
html = res.content.decode('utf-8')
#print(html)
reg = r'data-original="(.*?)"'#r表示当前的字符串不会被转义，是原始的字符串
url_list = re.findall(reg,html)#正则匹配的返回值为列表
#print(url_list)
for url in url_list:
    print(url)
    request.urlretrieve(url,'pic/%s' %(url.split('/')[-1]))
