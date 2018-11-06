# -*- coding: utf-8 -*-
import time
from check.initProxy import InitProxy
from check.refreshProxy import Refresh
from dbs.redisClient import RedisRefreshClient
from settings import REFRESH_TIME,RE_HTTP_LIMIT,RE_HTTPS_LIMIT


def init_db_2_db():
    init = InitProxy()
    init.run()


def refresh_item(scheme):
    ref = Refresh()
    ref.run(scheme)


db = RedisRefreshClient()


def check_manager():
    while True:
        http_count = db.count('http')
        https_count = db.count('https')
        if http_count < RE_HTTP_LIMIT or https_count < RE_HTTPS_LIMIT:
            init_db_2_db()
            time.sleep(8 * 60)
        refresh_item('http')
        time.sleep(10)
        refresh_item('https')
        time.sleep(REFRESH_TIME)


if __name__ == '__main__':
    # init_db_2_db()
    refresh_item('http')
    # refresh_item('https')
