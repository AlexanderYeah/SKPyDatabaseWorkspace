#coding=utf-8;

import pymysql




# 1 打开数据库
# 参数1 地址 参数2 用户名 参数2 密码 参数4 连接数据库的名字
# db = pymysql.connect("localhost","root","123456","oct_user");
#
# # 2 创建游标对象 进行操作数据库
# cursor = db.cursor();
#
# # 3 使用execute() 方法进行查询
# cursor.execute("SELECT VERSION()");
#
# # 4 使用fetchone() 获取单条数据
# data = cursor.fetchone();
#
# print("database version is %s"%data);


# 进行创建数据库表的操作
# 获取对象
db2 = pymysql.connect("localhost","root","123456","oct_user");
# 创建游标
cursor = db2.cursor();
# 使用execute 执行SQL 语句
cursor.execute("DROP TABLE IF EXISTS OCT_TEST1");
# 使用预处理语句创建表
sql = """CREATE TABLE OCT_TEST1(
        NAME CHAR(20) NOT NULL ,
        AGE INT ,
        SEX CHAR(1),
        INCOME FLOAT)""";

# 执行sql 语句
cursor.execute(sql);

# 关闭数据库
db2.close();


# 数据库创建完毕 ，然后进行插入数据
# 连接数据库
db3 = pymysql.connect("127.0.0.1","root","123456","oct_user");
# 获取游标
cursor =db3.cursor();
# sql 语句
sql3 = "INSERT INTO OCT_TEST1(NAME,AGE,SEX,INCOME)VALUES ('Alex','25','M',15000)"

# 执行sql 语句
try:
    cursor.execute(sql3);
    # 提交事务
    db3.commit();
except:
    # 发生错误进行告知
    print("insert table error");
    # 发生错误的时候 进行回滚
    db3.rollback();

# 执行关闭操作
db3.close();


#  数据库的查询操作
"""
    Nysql 使用 fetchone() 获取单挑数据
    fetchall() 获取多条数据
    rowcount 是一个只读的属性 ，返回执行execute之后影响的行数
"""
# 连接数据库
db4 = pymysql.connect("127.0.0.1","root","123456","oct_user");
# 获取游标
cursor = db4.cursor();
# SQL 语句
sql4 = "SELECT * FROM OCT_TEST1\
    WHERE INCOME > '%d'" %(10000);

try:
    # 执行sql 语句
    cursor.execute(sql4);
    # 获取所有记录列表
    res = cursor.fetchall();
    for row in res:
        name = row[0];
        age = row[1];
        sex = row[2];
        income = row[3];
        print("name=%s,age=%s,sex=%s,income=%s"%(name,age,sex,income));
except:
    print("select error happened");

# 关闭数据库
db4.close();














