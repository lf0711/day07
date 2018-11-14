# 修改默认日志文件名称
DEFAULT_LOG_FILENAME = '日志.log'    # 默认日志文件名称


# 配置要启动的爬虫
SPIDERS = [
    'spiders.baidu.BaiduSpider',
    'spiders.douban.DoubanSpider'
]

# 配置要启动管道
PIPELINES = [
    'pipelines.BaiduPipeline',
    'pipelines.DoubanPipeline'
]

# 配置要启动下载器中间件
# DOWNLOADER_MIDDLEWARES = [
#     'middleware.downloader_middleware.DownloaderMiddleware1',
#     'middleware.downloader_middleware.DownloaderMiddleware2'
# ]
#
# # 配置要启动爬虫中间件
# SPIDER_MIDDLEWARES = [
#     'middleware.spider_middleware.SpiderMiddleware1',
#     'middleware.spider_middleware.SpiderMiddleware2'
# ]