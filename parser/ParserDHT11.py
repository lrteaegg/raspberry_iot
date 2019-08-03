# encoding: utf-8
# DHT11 解析器
from Parser import AbstractParser
from utils.TimeUtils import TimeUtils


class ParserDHT11(AbstractParser):

    # 解析数据方法
    # return 字典
    def parse(self, data):
        humidity_bit = data[0:8]  # 分组
        humidity_point_bit = data[8:16]
        temperature_bit = data[16:24]
        temperature_point_bit = data[24:32]
        check_bit = data[32:40]
        humidity = 0
        humidity_point = 0
        temperature = 0
        temperature_point = 0
        check = 0
        for i in range(8):
            humidity += humidity_bit[i] * 2 ** (7 - i)  # 转换成十进制数据
            humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
            temperature += temperature_bit[i] * 2 ** (7 - i)
            temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
            check += check_bit[i] * 2 ** (7 - i)
        # tmp = humidity + humidity_point + temperature + temperature_point  # 十进制的数据相加
        return {'humidity': humidity, 'humidityPoint': humidity_point,
                'temperature': temperature, 'temperaturePoint': temperature_point,
                'check': check}

    # 转换成字节数组
    def parseBit(self, data_interval):
        data = []
        for i in data_interval[1:]:
            if i > 100:
                data.append(1)
            else:
                data.append(0)
        return data

    # 0011 0101+0000 0000+0001 1000+0000 0000= 0100 1101
    # 温度 + 湿度 = 校验码
    def check(self, dictionary):
        tmp = 0
        check = dictionary['check']
        for k,v in dictionary.items():
            tmp += v
        tmp -= check
        if check == tmp:
            # 数据校验，相等则输出
            # print "temperature : ", dictionary['temperature'], ", humidity : ", dictionary['humidity']
            return True
        else:  # 错误输出错误信息，和校验数据
            print "wrong"
            TimeUtils.timeSleep(0.5)
            # print "temperature : ", dictionary['temperature'], ", humidity : ", dictionary['humidity'], " check : ", check, " tmp : ", tmp
            return False