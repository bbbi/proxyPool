## ip代理池
- - -
#### 介绍文档
- ![](https://img.shields.io/badge/python-3.6-green.svg) ![](https://img.shields.io/badge/flask-1.0-blue.svg)
- requests爬取免费代理，flask提供web接口，redis存储代理
- 最新版本V1.0
 - 自动抓取ip
 - 对指定url进行筛选ip，实现http与https分类并区分代理质量
 - 提供web接口返回高质量的代理


#### 下载安装
- 下载代码

```shell
git clone https://github.com/bbbi/proxyPool.git
or
https://github.com/bbbi/proxyPool/archive/master.zip
```

- 安装依赖

```python
pip install -r requirements.txt
```

- 设置settings.py

```Python
# redis数据库设置
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
# API接口设置
API_HOST = '127.0.0.1'
API_PORT = 5000
```

- 启动

```Python
python3 run.py
# 启动成功的话会有4个进程分别启动不同的服务
```

#### 补充
- getter/proxyManager.py 中可以自行添加get静态函数
- 任何问题欢迎在[Issues](https://github.com/bbbi/proxyPool/issues)提出
- 本项目仅作为基本的代理池，不接收特有功能

#### 特别感谢
- [@jhao104](https://github.com/jhao104/proxy_pool) 和[@Germey ](https://github.com/Python3WebSpider/ProxyPool) 为我提供思路
