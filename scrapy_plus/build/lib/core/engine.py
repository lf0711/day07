"""
对各个模块进行调用
"""
from scrapy_plus.core.downloader import Downloader
from scrapy_plus.core.pipeline import Pipeline
from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.spider import Spider
from scrapy_plus.http1.request import Request


class Engine(object):
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.pipeline = Pipeline()
        self.downloader = Downloader()

    def start(self):
        """启动整个引擎,主要调用逻辑代码写在_start_engine中"""
        self._start_engine()

    def _start_engine(self):
        '''实现个业务之间对接'''
        # 爬虫模块发出初始化请求
        start_request = self.spider.start_request()
        # 把初始化请求添加给调度器
        self.scheduler.add_request(start_request)
        # 从调度器获取请求对象
        request = self.scheduler.get_request()
        # 调用下载器发送请求
        response = self.downloader.get_response(request)
        # 调用爬虫处理响应方法,处理响应,得到结果
        result = self.spider.parse(response)
        if isinstance(result,Request):
            self.scheduler.add_request(result)
        else:
            self.pipeline.process_item(result)
if __name__ == '__main__':
    spider_start = Engine()
    spider_start.start()