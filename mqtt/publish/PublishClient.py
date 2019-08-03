# encoding: utf-8

# 发布消息对象
class PublishClient(object):
    topic = 'test'
    QOS = 1
    client = None

    def __init__(self, topic, QOS, client):
        self.topic = topic
        self.QOS = QOS
        self.client = client

    # 发布消息
    def publish(self, data):
        # print '发送topic：', self.topic, " 发送内容：", data
        self.client.publish(self.topic, data, self.QOS)

    def setTopic(self, topic):
        self.topic = topic

    def setQOS(self, QOS):
        self.QOS = QOS



