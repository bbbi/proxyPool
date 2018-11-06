# -*- coding: utf-8 -*-
import time
from check.initProxy import InitProxy
from check.refreshProxy import Refresh
from dbs.redisClient import RedisRefreshClient
from settings import REFRESH_TIME,RE_HTTP_LIMIT,RE_HTTPS_LIMIT


def init_db_2_db():
    """
    init中的代理经检测放入存储库中
    :return:None
    """
    init = InitProxy()
    init.run()


def refresh_item(scheme):
    """
    数据库中的代理再检测
    :param scheme: 'http' or 'https'
    :return: None
    """
    ref = Refresh()
    ref.run(scheme)


db = RedisRefreshClient()


def check_manager():
    """
    检测模块运行管理
    :return: None
    """
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
