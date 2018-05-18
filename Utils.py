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


def adb_shell(cmd):
    return subprocess.call("adb shell " + cmd)


def screenshot():

    path = PATH(os.getcwd() + "/screenshot")
    if not os.path.isdir(path):
        os.makedirs(path)
    timestamp = time.strftime(
        '%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    timestamp = "tmp"

    source = (path + "/" + timestamp + ".png").replace("\\", "/")

    android_path = '/storage/emulated/0/Pictures/tmp.png'
    adb_shell("screencap -p " + android_path)
    CMD("adb pull " + android_path + " " + source)
    adb_shell("rm " + android_path)
    print("success " + source)


def getPosition(search):
    print("source " + source + "search " + search)
    img = cv2.cv2.imread(source, 0)
    template = cv2.cv2.imread(search, 0)
    sp = template.shape

    res = cv2.cv2.matchTemplate(img, template, cv2.cv2.TM_CCOEFF_NORMED)
    threshold = 0.99  # 匹配度
    if Const.TINGYUAN_TANSUO == search:
        threshold = 0.80  # 匹配度
    position = []

    loc = np.where(res >= threshold)  # 匹配程度大于%80的坐标y,x
    for pt in zip(*loc[::-1]):        # *号表示可选参数
        pos = [pt[0] + sp[1] * 0.5, pt[1] + sp[0] * 0.5]
        position.append(pos)

    return position


def tap(x, y):
    adb_shell("input tap " + str(x) + " " + str(y))


def swipe(deltax, deltay):
    print("滑动 " + str(deltax) + ", " + str(deltay))
    adb_shell("input swipe 640 320 " +
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
