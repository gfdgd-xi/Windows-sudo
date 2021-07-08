import os
import sys
try:
    if not os.path.exists(os.getenv("SystemDrive") + "\\Windows\\sudo.exe"):
        print("提示：你没有配置本程序，不需要卸载！")
        os.system("pause")
        sys.exit(0)
    try:
        os.mkdir(os.getenv("SystemDrive") + "\\Program Files\\temp")
        os.system("rd /S /Q \"{}\"".format(os.getenv("SystemDrive") + "\\Program Files\\temp"))
    except:
        print("提示：请使用管理员模式运行本程序！")
        os.system("pause")
        sys.exit(0)
    os.system("del \"{}\"".format(os.getenv("SystemDrive") + "\\Windows\\sudo.exe"))
    print("卸载完毕！")
    os.system("pause")
except:
    pass