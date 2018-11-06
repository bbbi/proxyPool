# -*- coding: utf-8 -*-


"""
代理评分规则
"""
# 代理质量最高评分
MAX_SCORE = 100
# 代理质量最低评分
MIN_SCORE = 0
# 初始评分
INITIAL_SCORE = 10
"""
代理检验设置
"""
CHECK_TIMEOUT = 10
CHECK_COUNT = 3
HTTPS_CHECK_URLS_TUPLE = (
    # "https://httpbin.org/ip",
    "https://www.baidu.com",
)
HTTP_CHECK_URLS_TUPLE = (
    # "http://httpbin.org/ip",
    "http://www.baidu.com",
)
"""
数据库
"""
# redis的IP地址
REDIS_HOST = "127.0.0.1"
# 端口
REDIS_PORT = 6379
# 数据库
REDIS_DB = 0
# 密码
REDIS_PASSWORD = None
# http存储redis键名
REDIS_KEY = "http_proxies"
# https存储键名
REDIS_HTTPS_KEY = "https_proxies"
# 暂存区redis键名
REDIS_INIT_KEY = "init_proxies"

"""
数据管理
"""
# init代理抓取时间（s）
INIT_TIME = 30 * 60
# init 限制
INIT_LIMIT = 1600
# refresh刷新时间
REFRESH_TIME = 10 * 60
RE_HTTP_LIMIT = 500
RE_HTTPS_LIMIT = 300

"""
API接口设置
"""
API_HOST = '127.0.0.1'
API_PORT = 5000

