import ctypes
import time
import winreg
import os
import sys
from utils import WifiFunction
from utils import init,parseSetting
from utils import WebFunction

filename = 'user_hait_setting'
desktop_path = "C:\\"  # 新创建的txt文件的存放路径
path = desktop_path + filename + '.txt'


if __name__ == '__main__':
    userId, userPwd, operator = init(path)
    url, header, data = parseSetting(userId, userPwd, operator)
    print(type(data))
    i = 1  # 若未连接进行五次循环
    while i <= 5:
        if WifiFunction.WifiConnet.getWifiStatus() == 4:  # wifi为连接状态，开始认证
            print('Wifi已连接，正在尝试认证...')
            print('正在进行第%d次连接...' % i)
            if WebFunction.WebPost(url, header, data).connect():  # 进行认证
                print('认证成功...')
                time.sleep(1)
                WifiFunction.ping_test(1)
                time.sleep(1)
                print('认证完成，程序将在15秒后退出')
                time.sleep(15)
                break
            else:
                print('认证失败，请查看返回信息,3秒后自动重连')
                time.sleep(3)
        else:
            print('Wifi未连接，正在连接校园网...')
            WifiFunction.WifiConnet.connectWifi()
        i += 1
    time.sleep(15)
