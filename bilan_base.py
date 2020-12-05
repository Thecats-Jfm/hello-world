import os
import random
import time
import cv2
import numpy as np
import win32api   #这些包用pycharm安装分分钟的事
TimeWait = 1
#连接mumu模拟器   首先先断开服务再执行连接
def Connection():
    cmd = 'adb kill-server'
    tmp = os.popen(cmd).readlines()
    cmd = 'adb connect 127.0.0.1:7555'
    tmp = os.popen(cmd).readlines()
    print(tmp)

#模拟点击   这个是代码的核心  也是繁琐的根源
def Click(x,y):
    cmd = 'adb shell input tap {x1} {y1}'.format(x1 = x,y1 = y)
    print(cmd)
    os.system(cmd)
