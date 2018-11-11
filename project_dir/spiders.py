# 继承框架中的爬虫类
from scrapy_plus.core.spider import Spider


class BaiduSpider(Spider):
    start_urls = [
        'http://www.baidu.com',
        'http://www.hao123.com'
    ]

