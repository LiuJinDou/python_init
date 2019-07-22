# coding=utf

import redis
#db = redis.Redis(host='127.0.0.1',port=6379,db=0,password='liuJindou')
db = redis.Redis(host='localhost',port=6379,db=0,auth='liuJindou')
db.set('name','test')
print r.get('name')
