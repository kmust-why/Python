from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from df_user.models import UserInfo
from hashlib import *
from df_user import user_decotator
from df_goods.models import GoodsInfo

# Create your views here.

def register(request):
    return render(request, 'df_user/register.html')

def register_handle(request):
    # 接收用户提交的值
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码是否一次
    if upwd != upwd:
        return redirect('/user/register/')

    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()

    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    # 注册成功，转到登录
    return redirect('/user/login/')

def login(request):
    uname = request.COOKIES.get('uname', 'a')
    context = {'error_name':0, 'error_pwd':0, 'uname':uname}
    return render(request, 'df_user/login.html', context)

def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    # 根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return  red
        else:
            context = {'error_name':0, 'error_pwd':0, 'uname':uname, 'upwd':upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)

# 等同于info = login(info)  info()
@user_decotator.login
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    for good_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(good_id)))
    context = {
        'user_email':user_email,
        'user_name':request.session['user_name'],
        'type': 'info',
        'goods_list':goods_list,
    }
    return render(request, 'df_user/user_center_info.html', context)

@user_decotator.login
def order(request):
    context = {'type':'order'}
    return render(request, 'df_user/user_center_order.html', context)

@user_decotator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'user':user, 'type': 'site'}
    return render(request, 'df_user/user_center_site.html', context)

def logout(request):
    request.session.flush()
    return redirect('/goods/index/')

