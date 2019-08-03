# encoding: utf-8
import time

class SleepTools(object):


    @staticmethod
    def delayMillisecond(ms):
        # 毫秒级的延迟
        time.sleep(ms*0.001)

    @staticmethod
    def delaySecond(second):
        # 秒级延迟
        time.sleep(second)

    @staticmethod
    def delayMicroSecond(microSecond):
        #微秒级的延迟
        time.sleep(microSecond*0.000001)