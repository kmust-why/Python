# flask进阶（Flask-Script）：

`Flask-Script`的作用是可以通过命令行的形式来操作`Flask`。例如通过命令跑一个开发版本的服务器、设置数据库，定时任务等。要使用`Flask-Script`，可以通过`pip install flask-script`安装最新版本。首先看一个最简单的例子：

```
# manage.py

from flask_script import Manager
from your_app import app

manager = Manager(app)

@manager.command
def hello():
    print 'hello'

if __name__ == '__main__':
    manager.run()

```

我们把脚本命令代码放在一个叫做`manage.py`文件中，然后在终端运行`python manage.py hello`命令，就可以看到输出`hello`了。

###### 定义命令的三种方法：

1. 使用`@command`装饰器：这种方法之前已经介绍过。就不过多讲解了。

2. 使用类继承自`Command`类：

   ```
   from flask_script import Command,Manager
   from your_app import app

   manager = Manager(app)

   class Hello(Command):
       "prints hello world"

       def run(self):
           print "hello world"

   manager.add_command('hello',Hello())

   ```

   使用类的方式，有三点需要注意：

   - 必须继承自`Command`基类。
   - 必须实现`run`方法。
   - 必须通过`add_command`方法添加命令。

3. 使用`option`装饰器：如果想要在使用命令的时候还传递参数进去，那么使用`@option`装饰器更加的方便：

   ```
   @manager.option('-n','--name',dest='name')
   def hello(name):
       print 'hello ',name

   ```

   这样，调用`hello`命令：

   ```
   python manage.py -n xt

   ```

   或者

   ```
   python manage.py --name xt

   ```

   就可以输出：

   ```
   hello xt

   ```

###### 添加参数到命令中：

- option装饰器：以上三种创建命令的方式都可以添加参数，

  ```
  @option
  ```

  装饰器，已经介绍过了。看以下示例介绍展示添加多个参数的方式：

  ```
  @manager.option('-n', '--name', dest='name', default='joe')
  @manager.option('-u', '--url', dest='url', default=None) 
  def hello(name, url): 
    if url is None: 
        print "hello", name 
    else: 
        print "hello", name, "from", url

  ```

- command装饰器：command装饰器也可以添加参数，但是不能那么的灵活，如下示例：

  ```
  @manager.command 
  def hello(name="Fred") 
    print "hello", name

  ```

- 类继承：类继承也可以添加参数，看以下示例：

  ```
    from flask_Flask import Comman,Manager,Option

    class Hello(Command):
        option_list = (
            Option('--name','-n',dest='name'),
        )

        def run(self,name):
            print "hello %s" % name

  ```

  如果要在指定参数的时候，动态的做一些事情，可以使用`get_options`方法，示例如下：

  ```
    class Hello(Command):
        def __init__(self,default_name='Joe'):
    self.default_name = default_name

        def get_options(self):
            return [
                Option('-n','--name',dest='name',default=self.default_name),
            ]

        def run(self,name):
            print 'hello',name
  ```