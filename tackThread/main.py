# encoding: utf-8
from CountDownLatch import CountDownLatch
# from SubThread import SubThread
import time
import datetime

from SleepTools import SleepTools

if __name__ == '__main__':
    # latch = CountDownLatch(2)
    # name = '!!'
    # print '开始%s'%name
    # start = time.clock()
    # thread1 = SubThread("thread1 ", latch,5)
    # thread2 = SubThread("thread2 ", latch, 1)
    # thread1.start()
    # thread2.start()
    # print '等待其他线程完成'
    # latch.await()
    # print 'stop main thread'
    # print 'Time used: ', (time.clock() - start)
    start = datetime.datetime.now()
    SleepTools.delaySecond(1)
    # SleepTools.delayMillisecond(1)
    # SleepTools.delayMicroSecond(1000)
    end = datetime.datetime.now()
    print end - start