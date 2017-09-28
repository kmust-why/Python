import web

urls = (
    '/','Index',
    '/upload/','Upload',
)

render = web.template.render('templates')

class Index():
    def GET(self):
        #return 'hello world'
        return render.index()

class Upload():
    def POST(self):
        i = web.input(file={})
        file = i.file.file.read()
        filename = i.file.filename
        with open(r'C:\Users\why\Desktop\django框架开发API接口\project\api_web\static\%s' %filename,'wb') as fn:
            fn.write(file)
        return 'http://127.0.0.1:8080/static/%s' %filename



if __name__ == '__main__':
    web.application(urls,globals()).run()