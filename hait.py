import os
import socket
import time
import requests
import sys
import winreg
import pywifi
from pywifi import const
import comtypes
#开机自启及取消自启
def add_to_startup(name,file_path=""):
	#By IvanHanloth
    if file_path == "":
        file_path = os.path.realpath(sys.argv[0])
    auth="IvanHanloth"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",winreg.KEY_SET_VALUE, winreg.KEY_ALL_ACCESS|winreg.KEY_WRITE|winreg.KEY_CREATE_SUB_KEY)#By IvanHanloth
    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, file_path)
    winreg.CloseKey(key)
def remove_from_startup(name):
    auth="IvanHanloth"
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", winreg.KEY_SET_VALUE, winreg.KEY_ALL_ACCESS|winreg.KEY_WRITE|winreg.KEY_CREATE_SUB_KEY)#By IvanHanloth
    try:
        winreg.DeleteValue(key, name)
    except FileNotFoundError:
        print(f"{name} not found in startup.")
    else:
        print(f"{name} removed from startup.")
    winreg.CloseKey(key)
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


filename = 'user_hait_setting'
desktop_path = "D:\\"  # 新创建的txt文件的存放路径
path = desktop_path + filename + '.txt'
is_new = False
try:
    with open(path) as f:
        s = f.read().strip().split()
    userId = s[0]
    userPwd = s[1]
    operator = s[2]
    iftrueopen = s[3]
    print(f'{userId}  {userPwd}  {operator}  {iftrueopen}')
    if(iftrueopen == 'false'):
        print(f'若需开机自启则删除{path}配置文件重新选择')
        if (iftrueopen == 'true'):
            print(f'若需关闭开机自启则删除{path}配置文件重新选择')
except FileNotFoundError:
    is_new = True
    print('当前为第一次使用')
    print(f'完成初始化之后，信息将被写入{path}中')
    userId = input('请输入学号：')
    userPwd = input('请输入密码：')
    operator = '@'
    iftrueopen = 'case'
    while True:
        cs = input(
                   '1.移动\n'
                   '2.联通\n'
                   '3.电信\n'
        '选择通信商(输入数字)：\n')
        match cs:
            case '1':
                operator = '@gxyyd'
                break
            case '2':
                operator = '@gxylt'
                break
            case '3':
                operator = '@gyxdx'
                break
            case _:
                print('输入值有误，请重新输入：')
    while True:
        choice = input(
            '是否开机自启，请选择\n'
            '1.是\n'
            '2.否（若已开启开机自启则选此选项删除）\n'
            '请输入数字：\n')
        match choice:
            case '1':
                iftrueopen = 'true'
                add_to_startup("hait_wifi")
                break
            case '2':
                iftrueopen = 'false'
                remove_from_startup("hait_wifi")
                break
            case _:
                print('输入值有误，请重新输入：')
    with open(path, 'wt') as w:
        w.write(f'{userId}\n{userPwd}\n{operator}\n{iftrueopen}')
        w.flush()
        print('初始化完成！')

hostIP = get_host_ip()
userName = userId + operator
url = 'http://211.69.15.33:9999/portalAuthAction.do'
# headers加上payload构成post请求
header = {
    'Host': '211.69.15.33:9999',
    'Connection': 'keep-alive',
    'Content-Length': '644',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://211.69.15.33:9999',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'http://211.69.15.33:9999/portalReceiveAction.do?wlanuserip={hostIP}&wlanacname=HAIT-SR8808',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'JSESSIONID=33529292B95C09300EE439374AAD0DBC.worker3'
}

data = {'wlanuserip': hostIP,
        'wlanacname': 'HAIT-SR8808',
        'chal_id': '',
        'chal_vector': '',
        'auth_type': 'PAP',
        'seq_id': '',
        'req_id': '',
        'wlanacIp': '172.21.8.73',
        'ssid': '',
        'vlan': '',
        'mac': '',
        'message': '',
        'bank_acct': '',
        'isCookies': '',
        'version': '0',
        'authkey': '88----89',
        'url': '',
        'usertime': '0',
        'listpasscode': '0',
        'listgetpass': '0',
        'getpasstype': '0',
        'randstr': '5099',
        'domain': '',
        'isRadiusProxy': 'true',
        'usertype': '0',
        'isHaveNotice': '0',
        'times': '12',
        'weizhi': '0',
        'smsid': '',
        'freeuser': '',
        'freepasswd': '',
        'listwxauth': '0',
        'templatetype': '1',
        'tname': 'gxy_pc_portal',
        'logintype': '0',
        'act': '',
        'is189': 'false',
        'terminalType': '',
        'checkterminal': 'true',
        'portalpageid': '23',
        'listfreeauth': '0',
        'viewlogin': '1',
        'userid': userName,
        'authGroupId': '',
        'smsoperatorsflat': '',
        'useridtemp': userName,
        'passwd': userPwd,
        'operator': operator,
        }
def connect():
    """进行认证\n
    认证成功->True\n
    其他设备在线->3秒后重新执行验证程序\n
    认证失败->False 并打印 网站源码"""
    req = requests.post(url, headers=header, data=data)
    req.encoding = req.apparent_encoding
    print(req.text)
    if '<title>校园黄页</title>' in req.text:
        return True
    elif url in req.url:
        print('3s后重新连接')
        time.sleep(3)
        connect()

    else:
        print(req.text)
        return False
    # 测试ping
def ping_test(url='www.baidu.com', n=1):
    ret = os.system("ping baidu.com -n 1")
    return True if ret == 0 else False
def wifi_connect_status():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # acquire the first Wlan card,maybe not

    if iface.status() in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:
        return 1
    else:
        print("wifi 未连接!")

    return 0
if __name__ == '__main__':
    print('当前ip地址为:', get_host_ip())
    i = 1  # 若未连接进行五次循环
    while i <= 5:
        if wifi_connect_status():  # wifi为连接状态，开始认证
            print('Wifi已连接，正在尝试认证...')
            print('正在进行第%d次连接...' % i)
            if connect():  # 进行认证
                print('认证成功...')
                time.sleep(1)
                ping_test()
                time.sleep(1)
                print('认证完成，程序将在15秒后退出')
                time.sleep(3)
                break
            else:
                print('认证失败，请查看返回信息：')
        else:
            print('WiFi未连接，请手动连接WiFi后，按回车键重新尝试连接')
            temp = input()
        i += 1
    time.sleep(15)
