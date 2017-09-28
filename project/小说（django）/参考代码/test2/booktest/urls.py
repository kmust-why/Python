from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#name='index'表示给该url取一个名为index的名字，用于反向解析
    url(r'^(\d+)/$', views.detail, name='detail'),
    url(r'^gettest1/$', views.gettest1, name='gettest1'),
    url(r'^gettest2/$', views.gettest2, name='gettest2'),
    url(r'^gettest3/$', views.gettest3, name='gettest3'),
    url(r'^getpost1/$', views.getpost1, name='getpost1'),
    url(r'^getpost2/$', views.getpost2, name='getpost2'),
    url(r'^cookietest/$', views.cookietest, name='cookietest'),
    url(r'^redirecttest/$', views.redirecttest, name='redirecttest'),
    url(r'^seesiontest1/$', views.seesiontest1, name='seesiontest1'),
    url(r'^seesiontest2/$', views.seesiontest2, name='seesiontest2'),
    url(r'^seesiontest3/$', views.seesiontest3, name='seesiontest3'),
    url(r'^session2_handle/$', views.session2_handle, name='session2_handle'),
    url(r'^objecttest/$', views.objecttest, name='objecttest'),
    url(r'^urltest/(\d+)/$', views.urltest, name='urltest'),
    url(r'^temptest/$', views.temptest, name='temptest'),
    url(r'^user1/$', views.user1, name='user1'),
    url(r'^user2/$', views.user2, name='user2'),
    url(r'^htmltest/$', views.htmltest, name='htmltest'),
    url(r'^csrf1/$', views.csrf1,name = 'csrf1'),
    url(r'^csrf2/$', views.csrf2,name = 'csrf2'),
    url(r'^verifyCode/$', views.verifyCode, name='verifyCode'),
    url(r'^imgtest/$', views.imgtest, name='imgtest'),
    url(r'^myExp/$', views.myExp, name='myExp'),
    url(r'^uploadPic/$', views.uploadPic, name='uploadPic'),
    url(r'^uploadHandle/$', views.uploadHandle, name='uploadHandle'),
    url(r'^herolist/(\d+)/$', views.herolist, name='herolist'),
    url(r'^area/$', views.area, name='area'),

]