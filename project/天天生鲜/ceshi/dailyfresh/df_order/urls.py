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
from df_order import views

urlpatterns = [
    url(r'^order/$', views.order, name='order'),
]
