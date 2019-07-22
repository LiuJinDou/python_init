#!/usr/bin/python
# -*- coding: utf8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1", "jindou", "", "test", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
#cursor.execute("SELECT VERSION()")
cursor.execute("SELECT * FROM user")

# 使用 fetchone() 方法获取一条数据
#data = cursor.fetchone()
data = cursor.fetchall()
#print "Database version : %s "
print data
print ('你好')
# 关闭数据库连接
db.close()
