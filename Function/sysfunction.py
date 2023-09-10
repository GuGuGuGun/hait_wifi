import os
import sys
import winreg


class SysFunction:
    def __init__(self,name,file_path=""):
        self.name = name
        self.file_path = file_path
    def add_to_startup(self, file_path=""):
        if file_path == "":
            file_path = os.path.realpath(sys.argv[0])
        auth = "IvanHanloth"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",
                             winreg.KEY_SET_VALUE,
                             winreg.KEY_ALL_ACCESS | winreg.KEY_WRITE | winreg.KEY_CREATE_SUB_KEY)
        winreg.SetValueEx(key, self.name, 0, winreg.REG_SZ, file_path)
        winreg.CloseKey(key)

    def remove_from_startup((self):
        auth = "IvanHanloth"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run",
                             winreg.KEY_SET_VALUE,
                             winreg.KEY_ALL_ACCESS | winreg.KEY_WRITE | winreg.KEY_CREATE_SUB_KEY)
        try:
            winreg.DeleteValue(key, self.name)
        except FileNotFoundError:
            print(f"{self.name} not found in startup.")
        else:
            print(f"{self.name} removed from startup.")
        winreg.CloseKey(key)
