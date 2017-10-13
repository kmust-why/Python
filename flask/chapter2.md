# 认识web

### url详解：

`URL`是`Uniform Resource Locator`的简写，统一资源定位符。

一个`URL`由以下几部分组成：

```
    scheme://host:port/path/?query-string=xxx#anchor

```

- **scheme**：代表的是访问的协议，一般为`http`或者`https`以及`ftp`等。
- **host**：主机名，域名，比如`www.baidu.com`。
- **port**：端口号。当你访问一个网站的时候，浏览器默认使用80端口。
- **path**：查找路径。比如：`www.jianshu.com/trending/now`，后面的`trending/now`就是`path`。
- **query-string**：查询字符串，比如：`www.baidu.com/s?wd=python`，后面的`wd=python`就是查询字符串。
- **anchor**：锚点，后台一般不用管，前端用来做页面定位的。

注意：`URL`中的所有字符都是`ASCII`字符集，如果出现非`ASCII`字符，比如中文，浏览器会进行编码再进行传输。

### web服务器和应用服务器以及web应用框架：

- **web服务器**：负责处理http请求，响应静态文件，常见的有`Apache`，`Nginx`以及微软的`IIS`.
- **应用服务器**：负责处理逻辑的服务器。比如`php`、`python`的代码，是不能直接通过`nginx`这种**web服务器**来处理的，只能通过**应用服务器**来处理，常见的应用服务器有`uwsgi`、`tomcat`等。
- **web应用框架**：一般使用某种语言，封装了常用的`web`功能的框架就是**web应用框架**，`flask`、`Django`以及Java中的`SSH(Structs2+Spring3+Hibernate3)`框架都是web应用框架。

### Content-type和Mime-type的作用和区别：

两者都是指定服务器和客户端之间传输数据的类型，区别如下：

- Content-type：既可以指定传输数据的类型，也可以指定数据的编码类型，例如：`text/html;charset=utf-8`
- Mime-type：不能指定传输的数据编码类型。例如：`text/html`

常用的数据类型如下：

- text/html（默认的，html文件）
- text/plain（纯文本）
- text/css（css文件）
- text/javascript（js文件）
- application/x-www-form-urlencoded（普通的表单提交）
- multipart/form-data（文件提交）
- application/json（json传输）
- application/xml（xml文件）