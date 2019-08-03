# -*- coding: utf-8 -*

import datetime
import Queue
from inductor.InductorDHT11 import DHT11
from parser.ParserDHT11 import ParserDHT11
from mqtt.publish.PublishClient import PublishClient
from factory.MQTTFactory import MQTTFactory
from tackThread.CountDownLatch import CountDownLatch
from tackThread.SubThread import TackThread
from tackThread.SubThread import SleepThread

if __name__ == '__main__':
    # 温湿度感应器数据
    dgt11Queue = Queue.Queue() # 生产者与消费者之间的消息传递，使用FIFO
    # 数据引脚
    pin = 26
    # 计时器
    latch = CountDownLatch(2)
    # 初始化感应器
    inductor = DHT11(pin)
    # 初始化解析器
    parser = ParserDHT11()
    # 设置感应器对应的解析器
    inductor.setParser(parser)
    # 初始化消息发布者
    publisher = PublishClient("test",1, MQTTFactory.getMQTTClient())
    print '欢迎使用'

    while True:
        # start = datetime.datetime.now()
        thread1 = TackThread("DHT11_Thread ", inductor, latch)
        thread2 = SleepThread("SleepThread-5s ", 5, latch)
        thread1.start()
        thread2.start()
        # print '等待其他线程完成'
        latch.await()
        # end = datetime.datetime.now()
        # 使用时间
        # print 'Time used: ', (end - start)
        result = thread1.getResult()
        # print 'Result:' , result

        dgt11Queue.put(result)
        # print 'queue size = ', dgt11Queue.qsize()
        if dgt11Queue.qsize() == 5:
            msg = inductor.package(dgt11Queue)
            # print 'packet',package
            print 'send msg = ', msg
            publisher.publish(msg)

        latch.setCount(2)