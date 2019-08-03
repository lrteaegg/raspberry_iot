# encoding:utf-8
# 解析器

class AbstractParser(object):
    # 解析收到的信息
    def parse(self, data):
        pass

    # 转换成字节数组
    def parseBit(self, data_interval):
        pass

    # 检查其数据的可靠性
    def check(self, dictionary):
        pass