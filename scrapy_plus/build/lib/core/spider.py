"""
对爬虫的分装
"""
from scrapy_plus.http1.request import Request
from scrapy_plus.item import Item


class Spider(object):
    """
    构造url
    解析响应对象
    """
    start_url = 'http://www.baidu.com'

    def start_request(self):
        """
        :return: 够在初始化对象并返回
        """
        return Request(self.start_url)

    def parse(self, response):
        """
        解析响应对象
        :param response:
        :return:
        """

        return Item(response.body)

