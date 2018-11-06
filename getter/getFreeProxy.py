# -*- coding: utf-8 -*-
import re
import time

from utils.utilFunc import getXpathHtml
from utils.webRequest import WebRequest


class GetFreeProxy:
    """
    获取免费的ip
    """

    def __init__(self):
        pass


    @staticmethod
    def OneXici(page=3):
        _url_list = []
        for page in range(1, page + 1):
            url = "http://www.xicidaili.com/nn/{}".format(str(page))
            _url_list.append(url)

        for url in _url_list:
            html = getXpathHtml(url)
            tr_list = html.xpath("//table[@id='ip_list']//tr")[1:]
            for tr in tr_list:
                item = {}
                ip = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) > 0 else ' '
                port = tr.xpath("./td[3]/text()")[0] if len(tr.xpath("./td[2]/text()")) > 0 else ' '
                item["proxy"] = ip + ':' + port
                item["scheme"] = tr.xpath("./td[6]/text()")[0].lower() if len(tr.xpath("./td[6]/text()")) > 0 else ' '
                yield item
    @staticmethod
    def Two66ip(page=3):
        wq = WebRequest()
        url_http = "http://www.66ip.cn/nmtq.php?getnum=50&proxytype=0&api=66ip"
        url_https = "http://www.66ip.cn/nmtq.php?getnum=50&proxytype=1&api=66ip"
        for _ in range(page):
            # 提取https代理
            response_https = wq.get(url=url_https)
            proxy_list1 = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}", response_https.text)
            for i in proxy_list1:
                item = {}
                item['proxy'] = i
                item['scheme'] = "https"
                yield item
            # 提取http代理
            response_http = wq.get(url=url_http)
            proxy_list2 = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}", response_http.text)
            for i in proxy_list2:
                item = {}
                item['proxy'] = i
                item['scheme'] = "http"
                yield item
    @staticmethod
    def ThreeKuaidaili(page=3):

        _temp_list = []
        for i in range(1, page + 1):
            url = "https://www.kuaidaili.com/free/inha/{}/".format(str(i))
            _temp_list.append(url)
        for url in _temp_list:
            html = getXpathHtml(url)
            time.sleep(3)
            tr_list = html.xpath("//div[@id='list']//tr")[1:]
            for tr in tr_list:
                item = {}
                ip = tr.xpath("./td[1]/text()")[0] if len(tr.xpath("./td[1]/text()")) > 0 else " "
                port = tr.xpath("./td[2]/text()")[0] if len(tr.xpath("./td[2]/text()")) > 0 else " "
                item["proxy"] = ip + ":" + port
                item["scheme"] = tr.xpath("./td[4]/text()")[0].lower() if len(tr.xpath("./td[4]/text()")) > 0 else " "
                yield item


if __name__ == '__main__':
    count = 1
    ip = GetFreeProxy()
    # for item in ip.OneXici():
    #     count += 1
    #     print(item)
    #
    # for item in ip.Two66ip():
    #     count += 1
    #     print(item)

    for item in ip.ThreeKuaidaili():
        count += 1
        print(item)
    print("共有：", count)
