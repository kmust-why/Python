from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
#处理首页请求
def index(request):
    #写这个页面的业务逻辑
    #return HttpResponse('hello why')
    return  render(request,'index.html')

#处理上传页面的请求
def upload(request):
    #写这个页面的业务逻辑
    if request.method == 'POST':
        #获取文件
        myfile = request.FILES.get('file')
        if not myfile:
            return JsonResponse({'result': 300,'success':'False','msg':'需选择文件再上传'})
        filename = myfile.name
        file = myfile.read()
        filesize = myfile.size
        if filesize == 0:
            return JsonResponse({'result': 400,'success':'False','msg':'上传的文件不能为空'})
        with open('upload/%s' %filename,'wb') as fn:
            fn.write(file)
        return  JsonResponse({'result':200,'success':'True','msg':'请求成功','path':'upload/%s' %filename})
    else:
        return JsonResponse({'result':403,'success':'False','msg':'不被允许的请求方式'})

def download(request,filename):
    file = open('upload/%s' %filename).read()
    response = HttpResponse(file)
    response['Content-type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s' %filename
    return response
