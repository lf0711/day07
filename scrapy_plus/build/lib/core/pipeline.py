"""
保存数据
"""
class Pipeline(object):
    def process_item(self,item):
        '''处理item对象'''
        print('item',item.data)