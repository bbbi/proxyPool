# -*- coding: utf-8 -*-
from threading import Thread

from check.checkProxy import checkProxy
from dbs.redisClient import RedisInitClient, RedisRefreshClient


class InitProxy:
    def __init__(self):
        self.init_db = RedisInitClient()
        self.db = RedisRefreshClient()

    def check(self):
        """
        检测代理，如果
        :return:
        """

        while True:
            print('init数据库剩余待检测代理', self.init_db.count())
            item = self.init_db.get()
            if not item:
                break
            result = checkProxy(item)
            if result:
                print(item, '检测通过添加到正式数据库,%s正式数据库数量' % item['scheme'], self.db.count(item['scheme']))
                self.db.add(item)

        return print("初始化代理已空，此轮检测结束")

    def run(self):
        t_list = []
        for i in range(7):
            print('检测线程已启动', i)
            t = Thread(target=self.check, name="checkThread%s" % i)
            t_list.append(t)

        for t in t_list:
            t.start()


if __name__ == '__main__':
    pass
