from tornado import web
from tornado import httpserver
from tornado import ioloop
import time

# 逻辑处理模块
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #print('这是get请求方式')
        #self.write('hello world.')
        t = time.ctime()
        self.render('index.html',time=t)
    def post(self, *args, **kwargs):
        pass

# 登陆的模块
class LoginHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        self.render('login.html')
    def get(self, *args, **kwargs):
        self.render('login.html')

# 路由与设置
application = web.Application([
    (r"/index", MainPageHandler),
    (r"/login", LoginHandler),
])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    print('http://127.0.0.1:8080')
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
