# -*- coding: utf-8 -*-
from queue import Queue
from threading import Thread
from check.checkProxy import checkProxy
from dbs.redisClient import RedisRefreshClient


class Refresh:
    def __init__(self):
        self.db = RedisRefreshClient()
        self.item_queue = Queue()

    def item_q(self, scheme):
        item_list = self.db.all(scheme)
        for item in item_list:
            self.item_queue.put(item)

    def refresh(self):
        while not self.item_queue.empty():
            print(self.item_queue.qsize())
            item = self.item_queue.get()
            result = checkProxy(item)
            if result:
                self.db.max(item)
                print("刷新通过设置为最高分", self.db.get_score(item))
            else:
                self.db.decrease(item)
                print("刷新未通过设置为减十分", self.db.get_score(item))
            self.item_queue.task_done()

        return print('此轮刷新已结束')

    def run(self, scheme):
        self.item_q(scheme)
        t_list = []
        for i in range(5):
            print("正式库刷新线程%s" % i)
            t = Thread(target=self.refresh)
            t_list.append(t)

        for t in t_list:
            t.start()


if __name__ == '__main__':
    pass
