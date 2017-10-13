# Flask-Migrate

在实际的开发环境中，经常会发生数据库修改的行为。一般我们修改数据库不会直接手动的去修改，而是去修改`ORM`对应的模型，然后再把模型映射到数据库中。这时候如果有一个工具能专门做这种事情，就显得非常有用了，而`flask-migrate`就是做这个事情的。`flask-migrate`是基于`Alembic`进行的一个封装，并集成到`Flask`中，而所有的迁移操作其实都是`Alembic`做的，他能跟踪模型的变化，并将变化映射到数据库中。

使用`Flask-Migrate`需要安装，命令如下：

```
​```python

```

pip install flask-migrate

```
​```

```

要让`Flask-Migrate`能够管理`app`中的数据库，需要使用`Migrate(app,db)`来绑定`app`和数据库。假如现在有以下`app`文件：

```
​```python

```

from flask import Flask from flask_sqlalchemy import SQLAlchemy from constants import DB_URI from flask_migrate import Migrate

app = Flask(**name**) app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True db = SQLAlchemy(app)

# 绑定app和数据库

migrate = Migrate(app,db)

class User(db.Model): id = db.Column(db.Integer,primary_key=True) username = db.Column(db.String(20))

```
addresses = db.relationship('Address',backref='user')

```

class Address(db.Model): id = db.Column(db.Integer,primary_key=True) email_address = db.Column(db.String(50)) user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

db.create_all()

@app.route('/') def hello_world(): return 'Hello World!'

if **name** == '**main**': app.run()

```
​```

```

之后，就可以在命令行中映射`ORM`了。要操作当前的`flask app`，首先需要将当前的`app`导入到环境变量中：

```
​```shell

```

# windows

$env:FLASK_APP='your_app.py'

# linux/unix

export FLASK_APP='your_app.py'

```
​```

```

将当前的`app`导入到环境变量中后，接下来就是需要初始化一个迁移文件夹：

```
​```shell

```

flask db init

```
​```

```

然后再把当前的模型添加到迁移文件中：

```
​```shell

```

flask db migrate

```
​```

```

最后再把迁移文件中对应的数据库操作，真正的映射到数据库中：

```
​```shell

```

flask db upgrade

```
​```

```

以上是通过加载当前的`app`到环境变量的做法，这种做法有点麻烦，每次都要设置环境变量。还有一种方法，可以直接通过`flask-script`的方式进行调用。现在重构之前的项目，设置为以下的目录结构： ![flaskmigrate项目目录结构](https://nunchakushuang.gitbooks.io/flask/content/assets/migrate%20.png) 以下对各个文件的作用进行解释：

**constants.py文件：**常量文件，用来存放数据库配置。

```
# constants.py
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'xt_flask_migrate'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

```

**ext.py文件：**把`db`变量放到一个单独的文件，而不是放在主`app`文件。这样做的目的是为了在大型项目中如果`db`被多个模型文件引用的话，会造成`from your_app import db`这样的方式，但是往往也在`your_app.py`中也会引入模型文件定义的类，这就造成了循环引用。所以最好的办法是把它放在不依赖其他模块的独立文件中。

```
# ext.py
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

```

**models.py文件：**模型文件，用来存放所有的模型，并且注意，因为这里使用的是`flask-script`的方式进行模型和表的映射，因此不需要使用`db.create_all()`的方式创建数据库。

```
# models.py
from ext import db
class User(db.Model): 
    id = db.Column(db.Integer,primary_key=True) 
    username = db.Column(db.String(50)) 
    addresses = db.relationship('Address',backref='user') 

    def __init__(self,username): 
        self.username = username

class Address(db.Model): 
    id = db.Column(db.Integer,primary_key=True) 
    email_address = db.Column(db.String(50)) 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) 

    def __init__(self,email_address): 
        self.email_address = email_address

```

**manage.py文件：**这个文件用来存放映射数据库的命令，`MigrateCommand`是`flask-migrate`集成的一个命令，因此想要添加到脚本命令中，需要采用`manager.add_command('db',MigrateCommand)`的方式，以后运行`python manage.py db xxx`的命令，其实就是执行`MigrateCommand`。

```
# manage.py
from flask_migrate import Migrate,MigrateCommand
from ext import db
from flask_script import Manager
from flask import Flask
from constants import DB_URI
import models
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__': 
    manager.run()

```

**flaskmigrate.py文件：**这个是主`app`文件，运行文件。并且因为`db`被放到另外一个文件中，所以使用`db.init_app(app)`的方式来绑定数据库。

```
# flaskmigrate.py
from flask import Flask
from ext import db

app = Flask(__name__)
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

```

之后运行命令来初始化迁移文件：

```
python manage.py db init

```

然后运行命令来将模型的映射添加到文件中：

```
python manage.py db migrate

```

最后添加将映射文件真正的映射到数据库中：

+

```
python manage.py db upgrade
```