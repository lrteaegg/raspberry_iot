# encoding: utf-8
# 温湿度感应器
from Inductor import AbstractInductor
import wiringpi
from utils.TimeUtils import TimeUtils
import json

class DHT11(AbstractInductor):
    # 初始化引脚
    def __init__(self, pin):
        self.pin = pin
        # 初始化引脚模块格式
        wiringpi.wiringPiSetupGpio()

    # 解析获取数据
    def parserData(self, dataInterval):
        dataBit = self.parser.parseBit(dataInterval)
        data = self.parser.parse(dataBit)
        if self.parser.check(data):
            data.update(createTime=TimeUtils.getSecondTimestamp())
            return data
        else:
            return False

    # 读取pin口数据
    def readPin(self):
        if (self.pin == ''):
            return ''
        dataInterval = []  # 获取时间间隔
        wiringpi.pinMode(self.pin, 1)
        wiringpi.digitalWrite(self.pin, 1)
        wiringpi.delay(50)  # 毫秒延时
        wiringpi.digitalWrite(self.pin, 0)
        wiringpi.delay(25)
        # 毫秒延时
        wiringpi.pinMode(self.pin, 0)
        for i in range(45):
            tc = wiringpi.micros()  # 返回当前的微秒数
            # 过滤掉前50ms的低电平
            while (wiringpi.digitalRead(self.pin) == 0):
                pass
            while (wiringpi.digitalRead(self.pin) == 1):
                if wiringpi.micros() - tc > 500:
                    break
            dataInterval.append(wiringpi.micros() - tc)
        # print dataInterval
        return dataInterval

    # Result: {'temperaturePoint': 3, 'temperature': 25, 'humidityPoint': 0, 'check': 69, 'createTime': 1564817626, 'humidity': 41}
    # 打包数据
    def package(self, queue):
        package = []
        while not queue.empty():
            item = queue.get()
            temperature = item['temperature']
            temperaturePoint = item['temperaturePoint']
            humidity = item['humidity']
            humidityPoint = item['humidityPoint']

            createTime = item['createTime']
            temp = temperature + 0.1*temperaturePoint
            hum = humidity + 0.1*humidityPoint
            package.extend([{'temperature':temp, 'humidity':hum, 'ts':createTime}])
        msg = json.dumps({
            "sn": "tp0000001",
            "data": package
        })
        return msg



