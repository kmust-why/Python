1. Tornado框架包含两个部分：socket和应用程序（路由）
2. 搭建tornado的socket服务器环境：
  - Tornado创建一个简单的http服务的固定写法：
```python
from tornado import web
from tornado import httpserver
from tornado import ioloop

class MainPageHandler(web.RequestHandler):
    pass

# 路由与设置
application = web.Application([
    (r"/", MainPageHandler),
])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
```
3. Python web开发工程师需要具备额条件：
  - 前端与后端

