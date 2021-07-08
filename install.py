import os
import sys
import shutil
import getpass
try:
    print("正在获取用户列表……")
    if os.path.exists(os.getenv("SystemDrive") + "\\Windows\\sudo.exe"):
        print("提示：你已经配置过本程序，请不要重复配置！")
        os.system("pause")
        sys.exit(0)
    try:
        os.mkdir(os.getenv("SystemDrive") + "\\Program Files\\temp")
        os.system("rd /S /Q \"{}\"".format(os.getenv("SystemDrive") + "\\Program Files\\temp"))
    except:
        print("提示：请使用管理员模式运行本程序！")
        os.system("pause")
        sys.exit(0)
    while True:
        print("请输入为此设置的密码（不要带双引号）：")
        #password = input("#>")
        password = getpass.getpass("#>")
        print("再输入一次：")
        passwordBak = getpass.getpass("#>")
        if password == passwordBak:
            break
    os.system("net user administrator /active:yes")
    os.system("net user administrator \"{}\"".format(password))
    os.system("copy \"{}\" \"{}\"".format(os.path.dirname(os.path.abspath(sys.argv[0])) + "\\sudo.exe", os.getenv("SystemDrive") + "\\Windows\\sudo.exe"))
    print("配置完毕！")
    os.system("pause")
except:
    pass