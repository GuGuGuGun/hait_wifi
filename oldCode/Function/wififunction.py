import os
import pywifi
from pywifi import const
import socket


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

class WifiFunction:
    def ping_test(url='www.baidu.com', n=1):
        ret = os.system("ping baidu.com -n 1")
        return True if ret == 0 else False

    def wifi_connect_status(self):
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]  # acquire the first Wlan card,maybe not

        if iface.status() in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:
            return 1
        else:
            print("wifi 未连接!")

        return 0
