#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: test_helper.py
#time: 2017/8/11 13:00
import MysqlHelper

#name = 'bbb'
#birthday = '1889-7-9'
#id = 1
#params = [name, birthday, id]
#params = [name]

#print(params)
#sql = 'update students set name=%s where id=%s'
#sql = "insert into students(name,birthday,gender) values(%s,%s,%s)"
#sql = 'delete from students where name=%s'
sql = "select * from students where id=1"
mysqlhelper = MysqlHelper.MysqlHelper(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='aa'
)
#mysqlhelper.cud(sql, params)
res = mysqlhelper.one(sql)
print(type(res))
print(res)

