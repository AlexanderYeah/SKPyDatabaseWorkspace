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
sql = """CREATE TABLE IF NOT EXISTS CLASS
    (ID INT PRIMARY KEY NOT NULL,
    NAME  TEXT NOT NULL ,
    AGE INT NOT  NULL
    )""";

cursor.execute(sql);
print("create Table successfully");
conn.commit();
conn.close();


# 插入数据
# conn1 = sqlite3.connect("test1.db");
# cursor1 = conn1.cursor();
# students = [(4,"Alexander",26),(5,"Tom",15),(6,"Green",87)];
# #  executemany 执行多次插入操作
# # execute 执行一次插入操作
# cursor1.executemany("INSERT INTO CLASS VALUES(?,?,?)",students);
# conn1.commit();
# conn1.close();


# 查询操作

conn2 = sqlite3.connect("test1.db");
cursor2 = conn2.cursor();

# # 查询一条记录 默认取第一条
# cursor2.execute("SELECT NAME FROM CLASS");
# # 取得一条数据
# res2 = cursor2.fetchone();
# print(res2);
#
# # 查询所有数据返回一个list
# cursor2.execute("SELECT * FROM CLASS WHERE  ID = 1");
# # 获取多条数据
# res2_many = cursor2.fetchall();
# print(res2_many);



#更新操作
cursor2.execute("UPDATE CLASS SET NAME = ? WHERE ID = ?",("YEAH",1));

# 删除操作
cursor2.execute("DELETE FROM CLASS WHERE ID = 4");

















