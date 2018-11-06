# -*- coding: utf-8 -*-
import time
from multiprocessing import Process

# api接口主函数
from api.proxyApi import api_run
# check模块主函数
from check.checkManager import check_manager
# getter模块主函数
from getter.proxyManager import get_manager


def pool_manager():
    p_api = Process(target=api_run, name='proxy_api')
    p_check = Process(target=check_manager, name='proxy_check')
    p_get = Process(target=get_manager, name='proxy_get')
    print('启动get')
    p_get.start()
    time.sleep(90)
    print('启动check')
    p_check.start()
    time.sleep(120)
    print('启动api')
    p_api.start()
    print('模块启动完成')
    p_get.join()
    p_check.join()
    p_api.join()
