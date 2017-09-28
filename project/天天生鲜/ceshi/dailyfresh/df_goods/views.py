from django.shortcuts import render
from df_goods.models import  TypeInfo, GoodsInfo
from django.core.paginator import Paginator, Page

# Create your views here.

def index(request):
    # 查询各分类最热和最新的4条数据
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'type0':type0,
        'type01': type01,
        'type1': type1,
        'type11': type11,
        'type2': type2,
        'type21': type21,
        'type3': type3,
        'type31': type31,
        'type4': type4,
        'type41': type41,
        'type5': type5,
        'type51': type51,
    }
    return render(request, 'df_goods/index.html', context)

def list(request, typeid, pagenum, sort):
    typeinfo = TypeInfo.objects.get(pk=int(typeid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':#默认，最新
        good_list = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by('-id')
    elif sort == '2':#价格
        good_list = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by('-gprice')
    elif sort == '3':#人气
        good_list = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by('-gclick')

    paginator = Paginator(good_list,1)
    # 获取当前页的数据
    page = paginator.page(int(pagenum))
    context = {
        'title':typeinfo.ttitle,
        'page':page,
        'paginator':paginator,
        'typeinfo':typeinfo,
        'sort':sort,
        'news':news,
    }
    return  render(request, 'df_goods/list.html', context)

def detail(request, id):
    good = GoodsInfo.objects.get(pk=int(id))
    good.gclick = good.gclick + 1
    good.save()
    news = good.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title':good.gtype.ttitle,
        'good':good,
        'news':news,
        'id':id,
    }
    response =  render(request, 'df_goods/detail.html', context)
    # 记录最近浏览信息，在用户中心使用
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_id = '%d'%good.id
    if goods_ids != '':#判断是否有浏览记录，如果有则继续判断
        goods_ids1 = goods_ids.split(',')# 拆分为列表
        if goods_ids1.count(goods_id) >= 1:# 如果商品已经被记录，则删除
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0, goods_id)# 添加到第一个
        # 如果超过3个则删除最后一个
        if len(goods_ids1) >= 4:
            del goods_ids1[3]
        goods_ids = ','.join(goods_ids1) #拼接为字符串
    else:
        goods_ids = goods_id #如果没有记录值，则直接加
    response.set_cookie('goods_ids', goods_ids)
    return  response


