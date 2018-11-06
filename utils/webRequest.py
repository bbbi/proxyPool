# -*- coding: utf-8 -*-
import time

import requests
from fake_useragent import UserAgent


class WebRequest:
    def __init__(self):
        pass

    @property
    def user_agent(self):
        return UserAgent().random

    @property
    def header(self):
        return {
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            "Accept-Encoding": "*/*",
            "Accept-Language": "zh-CN, zh;",
            "Connection": "keep-alive",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        }

    def get(self, url, proxy=None, cookies={}, retry_time=5, timeout=30, retry_count=3, ):

        headers = self.header
        status_code = [200, ]
        if headers:
            for i in range(retry_count):
                try:
                    response = requests.get(url, headers=headers, timeout=timeout, proxies=proxy, cookies=cookies)
                    if response.status_code in status_code:
                        return response

                except Exception as e:
                    print(e)
                    time.sleep(retry_time)
