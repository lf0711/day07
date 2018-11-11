"""
缓存url
url去重
"""
from six.moves.queue import Queue

class Scheduler(object):
    def __init__(self):
        self.queue = Queue()

    def add_request(self,request):
        """添加请求对象"""
        self.queue.put(request)

    def get_request(self):
        """获取一个请求对象并返回"""
        request = self.queue.get()
        return request

    def _filter_request(self):
        """请求去重"""
        pass


