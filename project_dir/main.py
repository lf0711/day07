from scrapy_plus.core.engine import Engine
from spiders.baidu import BaiduSpider
from spiders.douban import DoubanSpider
from spiders.pipelines import BaiduPipline
from spiders.pipelines import DoubanPipline



if __name__ == '__main__':
    baidu_spider = BaiduSpider()
    douban_spider = DoubanSpider()

    spiders = {
        BaiduSpider.name:baidu_spider,
        DoubanSpider.name:douban_spider
    }
    pipelines = [
        BaiduPipline(),
        DoubanPipline()
    ]

    engine = Engine(spiders,pipelines)
    engine.start()
