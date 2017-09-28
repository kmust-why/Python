from django.shortcuts import render
from test_postgresql.models import Member
from django.http import HttpResponse

# Create your views here.

def index(request):
    #操作数据库
    mem_list = Member.objects.order_by('?')[:5]
    for mem in mem_list:
        print('id=', mem.id, ',name=', mem.name, ',pwd=', mem.password, ',singal=', mem.singal, '\n')
    return  HttpResponse('hello python')


