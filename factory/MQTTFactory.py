# encoding: utf-8
import paho.mqtt.client as mqtt
# MQTT 客户端连接工厂
class MQTTFactory(object):
    HOST = '106.13.62.50'
    PORT = '1883'

    def on_connect(client, userdata, flags, rc):
        print '新客户端连接：'+client+", 连接状态:"+rc

    def on_message(client, userdata, msg):
        print "收到消息"+msg.topic + " " + msg.payload.decode("utf-8")

    # 获取连接
    @staticmethod
    def getMQTTClient():
        client = mqtt.Client()
        client.on_connect = MQTTFactory.on_connect
        client.on_message = MQTTFactory.on_message
        client.connect(MQTTFactory.HOST, MQTTFactory.PORT, 60)
        # client.loop_misc()
        client.loop_start()
        return client

    # 断开连接
    def closeConncet(self, client):
        client.loop_stop()

    def on_subscribe(client, userdata, mid, granted_qos):
        print client, userdata, mid, granted_qos

    def setHost(self, host):
        self.HOST = host

    def setPort(self, port):
        self.PORT = port

