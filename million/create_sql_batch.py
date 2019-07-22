# coding=utf-8

import random
import io
sql_file = io.open('/web/python/million/admin_batch.sql','w',encoding='utf-8')

_name = ['张三','里斯','王五','杨过','小龙女','晓东','如来','公爵','刘备','瑞贝','秦始皇','雍正','心如止水','送醉','丹雪','久念','影','坏小孩']
_len = 5000
while _len>=1:
    line = "INSERT INTO admin (name,sex,age) VALUES"
    val = []
    for i in range(1,1001):
        val.append((random.choice(_name),random.randint(0,1),random.randint(1,120)))
    _val = str(val)
    _sql = line+_val.strip('[]')
    sql_file.write(_sql+';\n')
    _len -=1
    
