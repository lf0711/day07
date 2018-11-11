class Response(object):
    """
    定义返回的响应内容
    """
    def __init__(self, url, status_code, headers, body):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body

