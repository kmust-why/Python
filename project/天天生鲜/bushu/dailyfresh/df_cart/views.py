from django.shortcuts import render,redirect
from django.http import JsonResponse
from df_user import user_decotator
from df_cart.models import CartInfo

# Create your views here.
@user_decotator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'carts':carts}
    return render(request, 'df_cart/cart.html', context)

@user_decotator.login
def add(request, gid, count):
    # 用户uid购买商品gid，数量为count
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + 1
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()
    if request.is_ajax():
        count = carts = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/cart/')

@user_decotator.login
def edit(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'carts':carts}
    return render(request, 'df_cart/cart.html', context)

@user_decotator.login
def delete(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'carts':carts}
    return render(request, 'df_cart/cart.html', context)


