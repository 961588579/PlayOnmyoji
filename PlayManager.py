#!/usr/bin/env python

import sys
import time
import _thread
import tkinter as tk
from tkinter import messagebox as mBox
from tkinter import Menu, Spinbox, scrolledtext, ttk

import Const
import Utils
from TanSuo import TanSuo
from YuHun import YuHun


class PlayManager:

    def __init__(self):
        self.autoPlay = False
        self.playMode = Const.PLAY_MODE.TANSUO
        self.tanSuo = TanSuo()
        self.yuHun = YuHun()

    def changeMode(self, mode):
        self.playMode = mode

    def playThread(self, threadName, delay):
        print("playThread")
        while True:
            time.sleep(3)
            print("autoPlay " + str(self.autoPlay))
            if self.autoPlay:
                try:
                    Utils.screenshot()
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    raise

                if Utils.find_and_click(Const.COMMON_WIN):
                    continue
                if Utils.find_and_click(Const.COMMON_END):
                    pass
                if Utils.find_and_click(Const.COMMON_LOSE):
                    pass

                if self.playMode == Const.PLAY_MODE.TANSUO:
                    self.tanSuo.doTanSuo()
                elif self.playMode == Const.PLAY_MODE.YUHUN:
                    self.yuHun.doYuHun()

    def startPlay(self):
        try:
            print("startPlay")
            _thread.start_new_thread(self.playThread, ("Thread-1", 2, ))
        except:
            print("Error: unable to start thread")
