from scrapy_plus.core.engine import Engine
from spiders.baidu import BaiduSpider
from spiders.douban import DoubanSpider
# from spiders.pipelines import BaiduPipline
# from spiders.pipelines import DoubanPipline
# from middlewares.spider_middlewares import TestSpiderMiddleware1,TestSpiderMiddleware2
# from middlewares.downloader_middlewares import TestDownloaderMiddleware1,TestDownloaderMiddleware2



if __name__ == '__main__':
    # baidu_spider = BaiduSpider()
    # douban_spider = DoubanSpider()
    # #
    # spiders = {
    #     BaiduSpider.name:baidu_spider,
    #     DoubanSpider.name:douban_spider
    # }
    # pipelines = [
    #     BaiduPipline(),
    #     DoubanPipline()
    # ]
    # spider_mids = [TestSpiderMiddleware1(),TestSpiderMiddleware2()]
    # downloader_mids = [TestDownloaderMiddleware1(),TestDownloaderMiddleware2()]

    engine = Engine()
    engine.start()
