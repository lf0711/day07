from scrapy_plus.core.engine import Engine
from spiders.spiders import BaiduSpider
from spiders.douban import DoubanSpider


if __name__ == '__main__':
    baidu_spider = BaiduSpider()
    douban_spider = DoubanSpider()

    spiders = {
        BaiduSpider.name:baidu_spider,
        DoubanSpider.name:douban_spider
    }
    engine = Engine(spider)
    engine.start()
