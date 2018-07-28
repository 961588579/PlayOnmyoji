#!/usr/bin/env python

import subprocess
import sys
import os
import time
import cv2
import numpy as np
import Const

source = "./screenshot/tmp.png"


def PATH(p):
    return os.path.abspath(p)


def CMD(cmd):
    return subprocess.call(cmd)


def adb(cmd):
    return subprocess.call("adb -s " + Const.DEVICE.MUMU + " " + cmd)


def adb_shell(cmd):
    return adb("shell " + cmd)


def screenshot():

    path = PATH("./screenshot")
    if not os.path.isdir(path):
        os.makedirs(path)

    android_path = '/storage/emulated/0/Pictures/tmp.png'
    adb("shell screencap -p " + android_path)
    adb("pull " + android_path + " " + source)
    adb("shell rm " + android_path)

    # 试图直接保存到电脑，然后失败了
    # save_path = (path + "/tmp.png").replace("\\", "/")
    # adb('shell screencap -p | ./sed \'s/\r$//\' > test.png')
    print("success " + path)


def getPosition(search):
    print("source " + source + " search " + search)
    if not os.path.exists(source) or not os.path.exists(search):
        return []
    img = cv2.cv2.imread(source, 0)
    template = cv2.cv2.imread(search, 0)
    sp = template.shape

    res = cv2.cv2.matchTemplate(img, template, cv2.cv2.TM_CCOEFF_NORMED)
    threshold = 0.90  # 匹配度
    if Const.TINGYUAN_TANSUO == search:
        threshold = 0.80  # 匹配度
    position = []

    loc = np.where(res >= threshold)  # 匹配程度大于%80的坐标y,x
    for pt in zip(*loc[::-1]):        # *号表示可选参数
        pos = [pt[0] + sp[1] * 0.5, pt[1] + sp[0] * 0.5]
        position.append(pos)

    return position


def tap(x, y):
    adb("shell input tap " + str(x) + " " + str(y))


def swipe(deltax, deltay):
    print("滑动 " + str(deltax) + ", " + str(deltay))
    adb("shell input swipe 640 320 " +
        str(640 + deltax) + " " + str(320 + deltay))


def find(search):
    posList = getPosition(search)
    if len(posList) > 0:
        return posList[0]
    return False


def find_and_click(search):
    posList = getPosition(search)
    if len(posList) > 0:
        pos = posList[0]
        print(search + ", 点击位置 " + str(pos))
        tap(pos[0], pos[1])
        return True
    return False
