# encoding: utf-8
from threading import Thread
# 引脚获取消息线程
from SleepTools import SleepTools

# 子线程
class TackThread(Thread):
    parser = None
    inductor = None

    def __init__(self, name, inductor, latch):
        Thread.__init__(self)
        self.name = name
        self.inductor = inductor
        self.latch = latch

    def run(self):
        # time.sleep(self.time)
        # print 'start industor %s' % self.name
        self.result = False
        while not self.result:
            dataInterval = self.inductor.readPin()
            self.result = self.inductor.parserData(dataInterval)
        self.latch.countDown()

    def setParser(self, parser):
        self.parser = parser

    def setInductor(self, inductor):
        self.inductor = inductor

    def getParser(self):
        return self.parser

    def getInductor(self):
        return self.inductor

    def getResult(self):
        return self.result

# 时间延迟线程
class SleepThread(Thread):

    def __init__(self, name, time, latch):
        Thread.__init__(self)
        self.name = name
        self.time = time
        self.latch = latch

    def run(self):
        # print 'thread name :', self.name
        SleepTools.delaySecond(self.time)
        # print 'start sleep %d' % self.time
        self.latch.countDown()


