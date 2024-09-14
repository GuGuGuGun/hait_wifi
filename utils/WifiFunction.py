import os
import socket
import subprocess
import sys
import time
import pywifi


class WifiConnet:

    iface = pywifi.PyWiFi().interfaces()[0]

    def __init__(self):
        self.iface = pywifi.PyWiFi().interfaces()[0]
        self.PREFIX = 'HAIT-Student'



    def findWifi(self, if_5G=False):
        iface = self.iface
        iface.scan()
        results = iface.scan_results()
        for result in results:
            if if_5G:
                if result.ssid.startswith(self.PREFIX + '-5G'):
                    return result.ssid
            else:
                if result.ssid.startswith(self.PREFIX):
                    return result.ssid
        return None

    @classmethod
    def getWifiStatus(cls):
        iface = cls.iface
        status = iface.status()
        return status

    @classmethod
    def connectWifi(cls,use_5G=True):
        fun = cls()
        if cls.getWifiStatus() == 4:
            print("当前已连接网络,无需再次连接")
            return True
        command = f'netsh wlan connect name="{fun.findWifi(use_5G)}"'
        subprocess.run(command,encoding='utf-8')

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def ping_test(url='www.baidu.com', n=1):
    ret = os.system("ping baidu.com -n 1")
    return True if ret == 0 else False

if __name__ == '__main__':
    print(get_host_ip())

