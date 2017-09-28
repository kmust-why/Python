from django.shortcuts import render
from django.http import HttpResponse
from novel.models import Novel
from novel.models import Chapter

# Create your views here.
def index(request):
    #return HttpResponse('hello python')
    # 获取数据库的内容
    novels = Novel.objects.filter().order_by('?')
    context = {
        'novels':novels,
    }
    return  render(request, template_name='index.html', context=context)

def detail(request,novelid):
    #novel = Novel.objects.filter(novelid=novelid)
    novel = Novel.objects.get(novelid=novelid)
    chapters = Chapter.objects.filter(novelid=novelid)
    context = {'novel': novel, 'chapters': chapters}
    return render(request, template_name='detail.html', context= context)

def chapter(request,chapterid):
    chapter = Chapter.objects.get(chapterid=chapterid)
    novel = Novel.objects.get(novelid=chapter.novelid)
    context = {'chapter': chapter, 'novel':novel}
    return render(request, template_name='chapter.html', context=context)
    #return HttpResponse('hello world')
