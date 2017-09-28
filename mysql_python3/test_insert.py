#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: test_insert.py
#time: 2017/8/11 10:50
import pymysql as sql
try:
    conn = sql.Connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'root',
        database = 'aa',
        charset='utf8'
    )
    cursor = conn.cursor()
    input_name = input('请输入用户名：')
    input_list = [input_name, "1994-4-5", 1]


    sql = "insert into students(name,birthday,gender) values('%s','%s',%s)" %(input_name, "1994-4-5", 1)
    print(sql)
    #sql = 'update students set name="李四" where name="gggg"'
    #sql = 'delete from students where name="李四"'
    #cursor.execute(sql, input_list)
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
except Exception as  e:
    print(e)
