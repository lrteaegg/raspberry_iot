from threading import Condition

class CountDownLatch:

    def __init__(self, count):
        self.count = count
        self.confition = Condition()

    def await(self):
        try:
            self.confition.acquire()
            while self.count > 0:
                self.confition.wait()
        finally:
            self.confition.release()

    def countDown(self):
        try:
            self.confition.acquire()
            self.count -= 1
            self.confition.notifyAll()
        finally:
            self.confition.release()

    def getCount(self):
        return self.count

    def setCount(self, count):
        self.count = count

