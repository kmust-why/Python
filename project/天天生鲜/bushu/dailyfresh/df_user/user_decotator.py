#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: wanghaiyun
@contact: 1563713769@qq.com
@software: PyCharm
@file: user_decotator.py
@time: 2017/8/6 8:27

"""
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# 如果未登录则，转到登录页面
# 等同于info = login(info)  info()
def login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return  func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())# 表示完整路径
            return red
    return login_fun

