import requests
import time

from utils import init, parseSetting


class WebPost:
    def __init__(self,url,header, data):
        self.url = url
        self.header = header
        self.data = data
    def connect(self):
        req = requests.post(self.url, headers=self.header, data=self.data)
        req.encoding = req.apparent_encoding
        spilt1 = req.text.split(",")
        print(spilt1[2])
        if '"message":null' in req.text:
            return True
        elif self.url in req.url:
            print('3s后重新连接')
            time.sleep(3)
            WebPost.connect(self)

        elif '"message":"AC999"' in req.text:
            print("当前已连接网络,无需再次连接")
            return True
        else:
            print(req.text)
            return False
