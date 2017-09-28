1. 创建scrapy项目

```shell
scrapy startproject my_spider
```

2. 创建爬虫类 （需要进入到爬虫目录下）

```shell
scrapy genspider itcast "http://www.itcast.cn"
```

3. 测试一个爬虫

```shell
scrapy check itcast
```

4. 运行一个爬虫

```shell
scrapy crawl itcast
```

5. 并发多个请求
6. Items.py表示可以定义我们需要的数据
7. piplines.py
8. 查看爬虫 scrapy list
9. 查看 scrapy crawl doutu
10. scrapy bench 测试scrapy的性能
11. scrapy fetch ‘www.baidu.com’爬去网站信息
12. crawl itcast -o itcast.json把输出导出到json文件中
13. crawl itcast -o itcast.csv把输出导出到csv文件中
14. 使用管道文件pipline