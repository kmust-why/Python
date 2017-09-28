from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from booktest.models import BookInfo
from booktest.models import HeroInfo
from django.core.paginator import *


# Create your views here.
def index(request):
    booklist = BookInfo.books1.all()
    context = {'booklist': booklist}
    print(request.path,request.method)
    return render(request,template_name='booktest/index.html',context=context)


def detail(request, id):
    book = BookInfo.books1.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'herolist': herolist}
    return render(request,template_name='booktest/detail.html',context=context)
#展示链接的页面
def gettest1(request):
    return render(request,template_name='booktest/gettest1.html')
#接收一键一值的情况
def gettest2(request):
    #print(request.GET['a'])
    # 接收一键一值的情况
    aa = request.GET['a']
    bb = request.GET['b']
    cc = request.GET['c']
    #构造上下文
    context = {'a':aa,'b':bb,'c':cc}
    #向模板中传递上下文，进行模板的渲染
    return render(request,template_name='booktest/gettest2.html',context=context)
#接收一键多值的情况
def gettest3(request):
    # 接收一键一值的情况
    #aa = request.GET['a']
    aa = request.GET.getlist('a')
    print(aa)
    # 构造上下文
    # 向模板中传递上下文，进行模板的渲染
    return render(request,template_name='booktest/gettest3.html')

def getpost1(request):
    return render(request, template_name='booktest/getpost1.html')

def getpost2(request):#控件的那name属性的值为键值，value属性的值为键值对应的value值
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}

    return render(request, template_name='booktest/getpost2.html',context=context)

#cookie练习
def cookietest(request):

    response = HttpResponse()
    Cookie = request.COOKIES
    #for key,value in Cookie:
     #   print(key,value)
    print(Cookie)

    #response.write(key+'->'+value+'\n')
    response.write('aa')
    #response = HttpResponse()
    #response.set_cookie('t1','abc')
    return response

#重定向练习
def redirecttest(request):
    #return HttpResponseRedirect('getpost1/')
    return redirect('getpost1/')

#通过用户登陆练习seesion
def seesiontest1(request):
    uname = request.session.get('uname','未登录')
    context = {'uname': uname}
    return render(request, template_name='booktest/seesiontest1.html', context=context)

def seesiontest2(request):
    return render(request, template_name='booktest/seesiontest2.html')

def seesiontest3(request):
    del request.session['uname']
    return redirect('/seesiontest1/')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['uname'] = uname
    return redirect('/seesiontest1/')

#在模板中使用对象
def objecttest(request):
    #hero = HeroInfo.objects.get(pk=3)
    hero = HeroInfo.objects.all()
    #hero = HeroInfo.objects.filter(isDelete=True)
    context = {'hero': hero}
    return render(request, template_name='booktest/objecttest.html', context=context)

def urltest(request,id):
    hero = HeroInfo.objects.all()
    context = {'id': id}
    return render(request, template_name='booktest/urltest.html', context=context)

#练习模板继承
def temptest(request):
    return render(request, template_name='booktest/base1.html')

def user1(request):
    return render(request, template_name='booktest/user1.html')

def user2(request):
    return render(request, template_name='booktest/user2.html')

def htmltest(request):
    context = {'t1':'<h1>abc</h1>'}
    return render(request, template_name='booktest/htmltest.html',context=context)

def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    uname=request.POST['uname']
    return render(request,'booktest/csrf2.html',{'uname':uname})

#验证码
def verifyCode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    #创建背景色
    bgColor=(random.randrange(50,100),random.randrange(50,100),0)
    #规定宽高
    width=100
    height=25
    #创建画布
    image=Image.new('RGB',(width,height),bgColor)
    #构造字体对象
    font=ImageFont.truetype('arial.ttf',24)
    #创建画笔
    draw=ImageDraw.Draw(image)
    #创建文本内容
    text='0123ABCD'
    #逐个绘制字符
    textTemp=''
    for i in range(4):
        textTemp1=text[random.randrange(0,len(text))]
        textTemp+=textTemp1
        draw.text((i*25,0),
            textTemp1,
            (255, 255, 255),
            font)
    request.session['code']=textTemp
    #保存到内存流中
    import io
    buf=io.StringIO()
    image.save(buf,'png')
    #将内存流中的内容输出到客户端
    return  HttpResponse(buf.getvalue(),'image/png')

def imgtest(request):
    return render(request, 'booktest/imgindex.html')

def myExp(reqeuest):
    a1=int('abc')
    return HttpResponse('hello')

def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

def uploadHandle(request):
    from django.conf import settings
    import os
    pic1=request.FILES['pic1']
    picName=os.path.join(settings.MEDIA_ROOT,'cc.jpg')
    with open(picName,'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    #return HttpResponse('<img src="/static/media/%s"/>'%pic1.name)
    return HttpResponse(picName)

#进行分页练习
def herolist(request,pindex):

    list = HeroInfo.objects.all()
    paginator = Paginator(list, 5)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'booktest/herolist.html', context)

#省市区选择
def area(request):
    return render(request,'booktest/area.html')
