#encoding:UTF-8
import urllib
import urllib.request

def getData(name):
    html = urllib.request.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=1' %name).read()


html = getData('love')
print(html)
