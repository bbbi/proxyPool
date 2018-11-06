# -*- coding: utf-8 -*-
import json

import redis

db = redis.StrictRedis(decode_responses=True)

# print(db.zadd('test2', 14, {"4": "1"}))
# print(db.zscore('test2', {'4': '1'}))
# print(db.zcard('test2'))
# print(db.zrevrangebyscore('test2', 100, 0))
# print([json.loads(i.replace("'", '"')) for i in db.zrevrangebyscore('test2', 100, 0)])
# print(db.zrange('test2', 0, 10))
print(db.zrangebyscore('http_proxies', 0, 100))
# a = db.spop('test1')
# a = a.replace("'",'"')
# print(a)
# print(type(a))
# b = json.loads(a)
# print(b)
# print(type(b))
