import sqlite3 #导入sqlite3模块

#用于数据库的连接，若不存在则创建一个新的数据库
conn = sqlite3.connect('C:\\Users\\why\\Desktop\\sqllite3\\code\\test.db')
#语句是一个字符串
sql_cmd = 'create table users(id int primary key not null, name text not null,age int not null)'

sql_insert = "insert into users values(1,'lisi',23,)"
conn.execute(sql_insert)

conn.close() #关闭连接