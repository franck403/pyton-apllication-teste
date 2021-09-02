import urllib.request
import time
from threading import Thread


class Telecharger(object):
    def __init__(self):
        self.count = 0
        self.block_size = 0
        self.total_size = 0

    def get_file(self):
        time.sleep(0.2)
        urllib.request.urlretrieve('http://www.oqapy.eu/releases/qarte-1.8.1.tar.gz', "qarte-1.8.1.tar.gz",
                                   self.reporthook)

    def reporthook(self, count, block_size, total_size):
        self.count = count
        self.block_size = block_size
        self.total_size = total_size


Tel = Telecharger()
Thread(target=Tel.get_file).start()

for i in range(10):
    time.sleep(0.10)
    print(Tel.count, Tel.block_size, Tel. urllib.request.urlretrieve('http://www.oqapy.eu/releases/qarte-1.8.1.tar.gz', "qarte-1.8.1.tar.gz", self.reporthook)
import time
from threading import Thread

class Telecharger(object):
    def __init__(self):
        self.count = 0
        self.block_size = 0
        self.total_size = 0

    def get_file(self):
        time.sleep(0.10)
        urllib.request.urlretrieve('http://www.oqapy.eu/releases/qarte-1.8.1.tar.gz', "qarte-1.8.1.tar.gz", self.reporthook)

    def reporthook(self, count, block_size, total_size):
        self.count = count
        self.block_size = block_size
        self.total_size =  total_size

Tel = Telecharger()
Thread(target=Tel.get_file).start()

for i in range(10):
    time.sleep(0.1)
    print(Tel.count, Tel.block_size, Tel.total_size)