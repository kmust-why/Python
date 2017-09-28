import requests
import re
from urllib import request

def get_url_list(url,reg):
    res = requests.get(url)
    html = res.content.decode('utf-8')
    #reg = r'data-mp4="(.*?)"'  # r表示当前的字符串不会被转义，是原始的字符串
    url_list = re.findall(reg, html)  # 正则匹配的返回值为列表
    return url_list


#获取源代码
#获取视频
for page in range(1,11):
    for url in get_url_list('http://www.budejie.com/video/',r'data-mp4="(.*?)"'):
        print(url)
        request.urlretrieve(url, '../video/%s' % (url.split('/')[-1]))

#获取图片

