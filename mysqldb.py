# coding=utf-8
import MySQLdb


def select(sql):
    # 打开数据库连接
    db = MySQLdb.connect(host="101.200.59.86", user="admin", passwd="Mkg999..", db="student", charset="utf8", port=3309)
    # db = MySQLdb.connect(host="localhost", user="root", passwd="root12", db="student", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句

    try:
        # 执行SQL语句

        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

        return results[0]







    except:
        print "Error:  unable to get mysql data"

    # 关闭数据库连接
    db.close()
