#!/usr/bin/env python
# encoding: utf-8

#version: 1.0
#author: wanghaiyun
#contact: 1563713769@qq.com
#file: test_insert.py
#time: 2017/8/11 10:50
import pymysql as sql


class MysqlHelper:
    def __init__(self, host, port, user, password, database, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
    def open(self):
        self.conn = sql.Connect(
            host = self.host ,
            port = self.port ,
            user = self.user,
            password = self.password,
            database = self.database,
            charset = self.charset
        )
        self.cursor = self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()
    def cud(self, sql, params):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()

            self.close()
        except Exception as e:
            print(e)

    def all(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return  result
        except Exception as e:
            print(e)
    def one(self, sql, params=[]):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
            return  result
        except Exception as e:
            print(e)

