# encoding: utf-8
# 感应器接口
class AbstractInductor(object):
    parser = None;

    # 设置解析器
    def setParser(self, parser):
        self.parser = parser

    # 解析从感应器中获取的数据
    def parserData(self, dataInterval):
        pass

    # 读取设备pin口数据
    def readPin(self, pin):
        pass

    # 打包数据
    def package(self, data):
        pass
