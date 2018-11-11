"""
保存数据
"""
class Pipeline(object):
    def process_item(self, item):
        '''处理item对象这里的data是item中的'''
        print('item:',item.data)