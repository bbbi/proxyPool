# -*- coding: utf-8 -*-
from proxy_pool_core.schedule import pool_manager


def run():
    print('代理池启动')
    pool_manager()
    print('启动完成')


if __name__ == '__main__':
    run()
