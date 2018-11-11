"""
封装request对象
"""


class Request(object):
    """
    定义请求参数
    """
    def __init__(self, url, method='GET', headers=None, params=None,data=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data

