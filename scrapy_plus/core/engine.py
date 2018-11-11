"""
对各个模块进行调用
"""
from datetime import datetime

from scrapy_plus.core.downloader import Downloader
from scrapy_plus.core.pipeline import Pipeline
from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.spider import Spider
from scrapy_plus.http1.request import Request
from scrapy_plus.middlewares.downloader_middlewares import DownloaderMiddleware
from scrapy_plus.middlewares.spider_middlewares import SpiderMiddleware
from scrapy_plus.utils.log import logger


class Engine(object):
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.pipeline = Pipeline()
        self.downloader = Downloader()
        self.spider_mid = SpiderMiddleware()  # 初始化爬虫中间件对象
        self.downloader_mid = DownloaderMiddleware()  # 初始化下载器中间件对象

    def start(self):
        """启动整个引擎,主要调用逻辑代码写在_start_engine中"""
        start = datetime.now()  # 获取当前时间
        logger.info('开始运行时间:%s' % start)
        self._start_engine()
        stop = datetime.now()
        logger.info('运行结束时间:%s' % stop)
        # 运行总耗时时间
        logger.info('耗时: %.2f' %(stop-start).total_seconds())

    def _start_engine(self):
        '''实现个业务之间对接'''
        # 爬虫模块发出初始化请求
        start_request = self.spider.start_request()

        # 爬虫中间件
        start_request=self.spider_mid.process_request(start_request)
        # 把初始化请求添加给调度器
        self.scheduler.add_request(start_request)
        # 从调度器获取请求对象
        request = self.scheduler.get_request()

        # 利用下载中间件预处理请求对象
        request = self.downloader_mid.process_request(request)
        # 调用下载器发送请求
        response = self.downloader.get_response(request)

        # 下载中间件预处理对象
        response = self.downloader_mid.process_response(response)
        # 调用爬虫处理响应方法,处理响应,得到结果
        result = self.spider.parse(response)
        if isinstance(result,Request):
            result = self.spider_mid.process_request(result)
            self.scheduler.add_request(result)
        else:
            self.pipeline.process_item(result)

if __name__ == '__main__':
    spider_start = Engine()
    spider_start.start()