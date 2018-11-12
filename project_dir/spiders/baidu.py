from scrapy_plus.core.spider import Spider

class BaiduSpider(Spider):

    name = 'baidou'

    start_urls = ['http://www.baidu.com','http://www.hao123.com']