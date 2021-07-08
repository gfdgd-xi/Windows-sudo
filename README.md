### 介绍

使用 Linux 有一段时间，听说 Windows 11 出了然后给自己的电脑安装了，但当我打开命令提示符并且需要使用管理员时，手贱敲了“sudo”，于是“'sudo' 不是内部或外部命令，也不是可运行的程序或批处理文件。”，有了写这个程序的想法。

### 安装

1、运行 install.py

手动安装：

1、启用 Administrator：

```bash
net user administrator /active:yes
``` 

2、为 Administrator 设置密码（如果已经设置密码请忽略<别设置中文密码>）：

```bash
net user administrator "密码"
```

3、把 `sudo.exe` 复制到 `C:\Windows` 下

### 卸载

1、运行 uninstall.py

手动卸载：

1、删除 `C:\Windows\sudo.exe`

### 安全性

杀毒软件会存在误报的情况，如果不放心可以自己使用 pyinstaller 打包可执行文件