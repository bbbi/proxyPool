# -*- coding: utf-8 -*-
import requests

from settings import HTTP_CHECK_URLS_TUPLE, HTTPS_CHECK_URLS_TUPLE, CHECK_COUNT, CHECK_TIMEOUT


def checkProxy(item={}):
    if item:
        if item['scheme'] == 'http':
            return checkHttp(item)
        elif item['scheme'] == 'https':
            return checkHttps(item)


def checkHttp(item):
    # 标记变量
    is_useful = False
    is_count = 0
    # 检验成功状态码
    status_code = [200, ]
    for url in HTTP_CHECK_URLS_TUPLE:
        count = len(HTTP_CHECK_URLS_TUPLE)
        for i in range(CHECK_COUNT):
            try:
                proxy = {
                    'http': item['scheme'] + '://' + item['proxy']
                }
                response = requests.get(url, timeout=CHECK_TIMEOUT, proxies=proxy)

                if response.status_code in status_code:
                    # print('http%s轮检测通过：' % i, response.text, proxy)
                    is_count += 1
                    break
            except Exception as e:
                print("http代理检测模块_检测未通过", item, e)
        if is_count == count:
            is_useful = True
    return is_useful


def checkHttps(item):
    # 标记变量
    is_useful = False
    is_count = 0
    # 检验成功状态码
    status_code = [200]
    for url in HTTPS_CHECK_URLS_TUPLE:
        count = len(HTTPS_CHECK_URLS_TUPLE)
        for i in range(CHECK_COUNT):
            try:
                proxy = {
                    'https': item['scheme'] + '://' + item['proxy']
                }
                response = requests.get(url, timeout=CHECK_TIMEOUT, proxies=proxy)
                if response.status_code in status_code:
                    is_count += 1
                    # print(response.text, item)
                    break
            except Exception as e:
                print("https代理检测模块_检测未通过", item, e)
        if is_count == count:
            is_useful = True

    return is_useful


if __name__ == '__main__':
    item_list = [

    ]
    for item in item_list:
        print(checkProxy(item))
