"""
实现多管道进行对数据的保存操作
"""
from spiders.baidu import BaiduSpider
from spiders.douban import DoubanSpider


class BaiduPipline(object):
    """需要增加参数爬虫对象来判断是哪个爬虫"""
    def process_item(self, item, spider):
        """处理item"""
        if isinstance(spider, BaiduSpider):
            print('百度爬虫的数据:', item)

        return item


class DoubanPipline(object):

    def process_item(self,item,spider):

        if spider.name == DoubanSpider.name:
            print('豆瓣爬虫的数据:', item)

        return item

