# -*- coding: utf-8 -*-
import time

from dbs.redisClient import RedisInitClient
from getter.getFreeProxy import GetFreeProxy
from settings import INIT_TIME,INIT_LIMIT

# 所有获取代理生成器列表
generator_list = [
    GetFreeProxy.OneXici(),
    GetFreeProxy.Two66ip(),
    GetFreeProxy.ThreeKuaidaili(),
]

db = RedisInitClient()


def get_proxy_2_init_db():
    for i in generator_list:
        for item in i:
            db.add(item)


def get_manager():
    while True:
        count = db.count()
        if count < INIT_LIMIT:
            # 获取代理
            get_proxy_2_init_db()
        # 获取时间
        time.sleep(INIT_TIME)


if __name__ == '__main__':
    get_proxy_2_init_db()
