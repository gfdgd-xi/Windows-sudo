##########################
# 引入库
##########################
import os
import sys
##########################
# 获取命令或参数
##########################
try:
    list = sys.argv
    if len(list) <= 1 or "--help" in list:
        print("帮助：")
        print("应用提权")
        print("使用方法：sudo 参数（参数不要带双引号）")
        sys.exit(0)
    list.pop(0)
    command = 'runas /user:administrator "'
    for i in list:
        command = command + i + " "
    command = command + '"'
    os.system(command)
except:
    pass