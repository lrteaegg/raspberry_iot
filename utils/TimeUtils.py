# encoding: utf-8
import time

class TimeUtils(object):

    # 获取秒级的时间戳
    @staticmethod
    def getSecondTimestamp():
        return int(time.time());

    # 获取毫秒级的时间戳
    @staticmethod
    def getMillisecondTimestamp():
        return int(round(time.time() * 1000));

    @staticmethod
    def timeSleep(delay):
        time.sleep(delay)


