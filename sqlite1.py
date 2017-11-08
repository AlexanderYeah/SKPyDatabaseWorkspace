#coding=utf-8;

import sqlite3

"""
    Python 2.5 以来，引入了SQLite 数据库适配器将其作为sqlite3 模块，纳入自己的标准库
    以为SQlite 使得开发更加迅速，不需要服务器，也米有许可证的问题

    python 中直接使用即可，如果数据库不存在 就会被创建

"""

#1  连接数据库 不存在就会被创建,一旦创建成功，就会出现在当前目录下面

conn = sqlite3.connect("test1.db");

print("open db successfully");

#2 创建表格

# 创建游标
cursor = conn.cursor();
# sql 语句
sql = """CREATE TABLE CLASS
    (ID INT PRIMARY KEY NOT NULL,
    NAME  TEXT NOT NULL ,
    AGE INT NOT  NULL
    )""";

cursor.execute(sql);
print("create Table successfully");
conn.commit();
conn.close();




