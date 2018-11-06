# -*- coding: utf-8 -*-
import re

from lxml import etree

from utils.webRequest import WebRequest


def verifyProxyFormat(proxy):
    """
    核实代理地址的格式
    :param proxy: 待检测代理
    :return: 核验结果
    """
    verify_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    _temp = re.match(verify_regex, proxy)
    return not _temp == None


def getXpathHtml(url, **kwargs):
    """
    得到etree后的结果
    :param url:
    :param kwargs:
    :return:
    """
    wq = WebRequest()
    response = wq.get(url)
    return etree.HTML(response.content)


if __name__ == '__main__':
    # print(verifyProxyFormat("60.186.70.134:111"))

    html = getXpathHtml("https://www.kuaidaili.com/free/inha/2 ")
    print(html.xpath('//text()'))
