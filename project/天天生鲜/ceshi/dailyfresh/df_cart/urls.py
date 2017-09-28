#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: wanghaiyun
@contact: 1563713769@qq.com
@software: PyCharm
@file: urls.py
@time: 2017/8/6 13:43

"""
from django.conf.urls import url
from df_cart import views

urlpatterns = [
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^add(\d+)_(\d+)/$', views.add, name='add'),
    url(r'^edit(\d+)_(\d+)/$', views.edit, name='edit'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
]
