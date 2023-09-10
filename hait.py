import time
from Function import webfunction
from Function import sysfunction
from Function import wififunction


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
    if (iftrueopen == 'false'):
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
                sysfunction.SysFunction.add_to_startup("hait_wifi")
                break
            case '2':
                iftrueopen = 'false'
                sysfunction.SysFunction.remove_from_startup("hait_wifi")
                break
            case _:
                print('输入值有误，请重新输入：')
    with open(path, 'wt') as w:
        w.write(f'{userId}\n{userPwd}\n{operator}\n{iftrueopen}')
        w.flush()
        print('初始化完成！')

hostIP = wififunction.get_host_ip()
userName = userId + operator
url = f'http://211.69.15.10:6060/quickauth.do?'
# headers加上payload构成post请求

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'b-user-id=977405d8-0e5e-8a72-ad4d-29a4a54ce195; macAuth=',
    'Host': '211.69.15.10:6060',
    'Referer': f'http://211.69.15.10:6060/portalReceiveAction.do?wlanuserip={hostIP}&wlanacname=HAIT-SR8808',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'userid': userName,
    'passwd': userPwd,
    'wlanuserip': hostIP,
    'wlanacname': 'HAIT-SR8808',
    'wlanacIp': '172.21.8.73',
    'ssid': '',
    'vlan': '',
    'mac': '',
    'version': '0',
    'portalpageid': '21',
    'portaltype': '0',
    'hostname': '',
    'bindCtrlId': '',
}


if __name__ == '__main__':
    print('当前ip地址为:', wififunction.get_host_ip())
    i = 1  # 若未连接进行五次循环
    while i <= 5:
        if wififunction.WifiFunction.wifi_connect_status(1):  # wifi为连接状态，开始认证
            print('Wifi已连接，正在尝试认证...')
            print('正在进行第%d次连接...' % i)
            if webfunction.WebPost(url,header, data).connect():  # 进行认证
                print('认证成功...')
                time.sleep(1)
                wififunction.WifiFunction.ping_test(1)
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
