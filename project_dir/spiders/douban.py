from scrapy_plus.core.spider import Spider
from scrapy_plus.http1.request import Request
from scrapy_plus.item import Item


class DoubanSpider(Spider):

    name = "douban"

    def start_request(self):
        """
        :return: 够在初始化对象并返回
        """
        start_urls1 = 'https://movie.douban.com/top250?start={}&filter='
        for a in range(0, 225, 25):
            start_urls = start_urls1.format(a)
            yield Request(start_urls)

    def parse(self, response):
        """
        解析响应对象
        :param response:
        :return:
        """
        a_s = response.xpath('//div[@class="hd"]/a')
        for a in a_s:
            data = {}
            data['movie_name'] = a.xpath('./span[1]/text()')[0]
            data['movie_url'] = a.xpath('./@href')[0]
            # print(data)
            # yield Item(data)
            yield Request(data['movie_url'], callback=self.parse_detail, meta={'data': data} )
            # yield Item(data)
        # return Item(response.url)

    def parse_detail(self,response):
        """解析详情页数据"""
        data = response.meta['data']
        # print(data)
        data['movie_length'] = response.xpath('//span[@property="v:runtime"]/text()')[0]
        print(data)
        yield Item(data)


