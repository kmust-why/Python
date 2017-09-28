from django.conf.urls import url
from df_goods import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
]
