from django.shortcuts import render

from novel.models import Novel
from novel.models import Chapter
# Create your views here.视图文件
from django.http import HttpResponse
def index(request): #用来访问响应首页的请求
    #return HttpResponse('hello world')
    #novel = Novel.objects.filter(novelid=1)
    novel = Novel.objects.order_by('?')[:30]
    return render(request,template_name='index.html',context={'novels':novel})

def novel_list(request,novelid):
    novel = Novel.objects.filter(novelid=novelid)
    chapters = Chapter.objects.filter(novelid=novelid)
    return render(request, template_name='chapter.html', context={'novel': novel,'chapters':chapters})

def chapter_list(request,chapterid):
    chapter = Chapter.objects.get(chapterid=chapterid)
    return render(request, template_name='content.html', context={'chapter':chapter})
    #return HttpResponse('hello world')