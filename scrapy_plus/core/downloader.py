"""
下载器组件,发起请求获取响应
"""
import requests

from scrapy_plus.http1.response import Response


class Downloader(object):

    def get_response(self,request):
        '''发起请求获取想响应的方法'''
        # 判断请求对象,发起请求,获取响应
        # 判断请求方法
        if request.method.upper() == 'GET':
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, headers=request.headers,data=request.data)
        else:
            raise Exception('目前只支持get和post请求')

        return Response(resp.url, resp.status_code, resp.headers, resp.content)