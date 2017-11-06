#coding=utf-8;
import pymysql


# 打开数据库
db = pymysql.connect("127.0.0.1","root","123456","oct_user");
# 获取游标
cursor1 = db.cursor();
# SQL 语句
sql1 = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    # 执行sql 语句
    cursor1.execute(sql1);
    # 提交事务
    cursor1.commit();
except:
    # 发生错误进行回滚
    print("ERROR Happen");
    db.rollback();

# 关闭数据库、
db.close();


