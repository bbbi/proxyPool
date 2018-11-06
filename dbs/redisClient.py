# -*- coding: utf-8 -*-
import json
from random import choice

import redis

import settings


class RedisInitClient:
    def __init__(self, host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB,
                 password=settings.REDIS_PASSWORD):
        """
        初始化连接redis数据库
        :param host: 数据库IP
        :param port: 数据库端口
        :param db: 数据库编号
        :param password: 数据库密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)

    def add(self, item):
        """
        向初始化数据库中添加数据
        :param proxy: 待检测代理
        :return: 返回添加结果
        """
        return self.db.sadd(settings.REDIS_INIT_KEY, item)

    def get(self):
        """
        获取一个redis数据库中的数据
        :return: 返回一个dict格式的数据
        """
        item = self.db.spop(settings.REDIS_INIT_KEY)
        if item:
            item = json.loads(item.replace("'", '"'))
        return item

    def count(self):
        """
        返回多有初始化库中的代理数量
        :return:代理数量
        """
        return self.db.scard(settings.REDIS_INIT_KEY)


class RedisRefreshClient:
    def __init__(self, host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB,
                 password=settings.REDIS_PASSWORD):
        """
        初始化连接redis数据库
        :param host: 数据库IP
        :param port: 数据库端口
        :param db: 数据库编号
        :param password: 数据库密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)

    def add(self, item, score=settings.INITIAL_SCORE):
        """
        向数据库中添加代理
        :param item: 代理
        :param score: 插入代理时的初始化
        :return:返回插入结果
        """
        if item['scheme'] == "https":
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY

        if not self.db.zscore(key, item):
            return self.db.zadd(key, score, item)

    def random(self, scheme):
        """
        随机获取有效的代理，如果有最高分，随机取最高分，如果没有最高分按分数随机取80-100之间的，否则返回None
        :return: 返回随机代理
        """
        if scheme == 'https':
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY
        result = self.db.zrangebyscore(key, settings.MAX_SCORE, settings.MAX_SCORE)
        if len(result):
            item = json.loads(choice(result).replace("'", '"'))
            return item
        else:
            result = self.db.zrevrangebyscore(key, 100, 0)
            if len(result):
                item = json.loads(choice(result).replace("'", '"'))
                return item
            else:
                return None

    def decrease(self, item):
        """
        代理减分，如果为0 则移除这个代理
        :param item: 代理
        :return: 修改结果
        """
        if item['scheme'] == "https":
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY

        score = self.db.zscore(key, item)

        if score and score > settings.MIN_SCORE:
            return self.db.zincrby(key, item, -10)
        else:
            return self.db.zrem(key, item)

    def exists(self, item):
        """
        判断代理是否存在
        :param item: 代理
        :return: 存在返回True
        """
        if item['scheme'] == "https":
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY
        return not self.db.zscore(key, item) == None

    def get_score(self, item):

        if item['scheme'] == "https":
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY
        result = self.db.zscore(key, item)
        if result:
            return result
        else:
            return '此记录已经删除'

    def max(self, item):
        """
        将代理设置为最大分数
        :param item: 代理
        :return: 设置结果
        """
        if item['scheme'] == "https":
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY
        return self.db.zadd(key, settings.MAX_SCORE, item)

    def count(self, scheme):
        """
        获取代理的数量
        :return: 数量
        """
        if scheme == "https":
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY
        return self.db.zcard(key)

    def all(self, scheme):
        """
        获取所有的代理
        :return: 全部的代理列表
        """
        if scheme == "https":
            key = settings.REDIS_HTTPS_KEY
        else:
            key = settings.REDIS_KEY
        print(key)
        return [json.loads(i.replace("'", '"')) for i in
                self.db.zrangebyscore(key, settings.MIN_SCORE, settings.MAX_SCORE)]


if __name__ == '__main__':
    db = RedisRefreshClient()
    print()
    print(db.all('http'))
