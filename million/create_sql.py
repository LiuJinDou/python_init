# coding=utf-8

import random
import io
sql_file = io.open('/web/python/million/admin.sql','w',encoding='utf-8')

_name = ['张三','里斯','王五','杨过']
_len = 5000000
while _len>0:
    line = "INSERT INTO admin(name,sex,age) VALUES ('%s',%d,%d);"%(random.choice(_name),random.randint(0,1),random.randint(0,120))
    sql_file.write(line+'\n')
    _len -=1
    
