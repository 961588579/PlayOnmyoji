#!/usr/bin/env python

import sys
import time
import Utils
from TanSuo import TanSuo
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as mBox

autoPlay = True

if __name__ == "__main__":
    tanSuo = TanSuo()

    Utils.CMD("adb connect 127.0.0.1:7555")
    Utils.CMD("adb wait-for-device")

    while autoPlay:
        try:
            Utils.screenshot()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

        if Utils.find_and_click('./res/end.png'):
            continue
        elif Utils.find('./res/tansuo/flag.png'):
            print("在探索界面")
            tanSuo.doTanSuo()
        else:
            tanSuo.doEnterTanSuo(25)

        time.sleep(3)
