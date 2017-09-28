#coding = 'utf-8'
import urllib,re
from bs4 import BeautifulSoup #解析源码
import urllib.request
import html.parser

#获取源码
def getContentOrComment(Url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}

    request = urllib.request.Request(url=Url, headers=header)
    try:
        response = urllib.request.urlopen(request)  # 打开网址
        text = response.read().decode('UTF-8')  # 获取所有的源码
    except Exception as e:
        text = None
    #print(text)
    return text
#文章地址
articleUrl = 'http://www.qiushibaike.com/textnew/page/%d'
#评论地址
commentUrl = 'http://www.qiushibaike.com/article/%s'
page = 0
while True:
    raw = input('点击enter查看或者输入exit退出，请输入你的选择：')
    if raw == 'exit':
        break #跳出循环
    page += 1
    Url = articleUrl % page


    articlePage = getContentOrComment(Url)
    articleFloor = 1
    #print(articlePage)

    #print('kkkk')
    #获取段子内容
    soupArticle = BeautifulSoup(articlePage,'html.parser')#解析网页
    #print('gggg')
    #print(soupArticle)
    for string in soupArticle.find_all(attrs = "article block untagged mb15"):
        commentId = str(string.get('id')).strip()[11:]
        #print('ffff')
        #print(commentId)
        print(articleFloor,'.',string.find(attrs = "content").get_text().strip())
        articleFloor += 1

        #获取评论
        commentPage = getContentOrComment(commentUrl % commentId)
        if commentPage is None:
            continue
        soupComment = BeautifulSoup(commentPage,'hmtl.parser')#解析网页
        commentFloor = 1
        for comment in soupComment.find_all(attrs="body"):
            #print('ffff')
            # print(commentId)
            print('      ',commentFloor, '楼回复',
                  comment.get_text().strip())
            commentFloor += 1