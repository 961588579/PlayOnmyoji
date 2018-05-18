#!/usr/bin/env python

import time

import Const
import Utils


class TanSuo:

    def __init__(self):
        # 用来记录探索时拖动的方向 1 手指从右向左   -1 手指从左向右
        self.tansuoDirector = 1
        # 用来记录探索时拖动的偏移，范围在-2048~2048
        self.tansuoDeltaX = 0

    def doTanSuo(self):

        if Utils.find(Const.TANSUO_FLAG):
            print("在探索界面")
            # 探索Boss
            if Utils.find_and_click(Const.TANSUO_BOSS):
                return
            # 探索小怪
            if Utils.find_and_click(Const.TANSUO_ENEMY):
                return
            if Utils.find_and_click(Const.TANSUO_REWARD):
                return
            pos = Utils.find(Const.TANSUO_GETREWARD)
            if pos != False:
                Utils.tap(pos[0], pos[1] + 360)
            else:
                print("啥也没有，滑一滑")
                deltax = self.tansuoDirector * 640
                self.tansuoDeltaX += deltax
                Utils.swipe(deltax, 0)
                if self.tansuoDeltaX > 2048:
                    self.tansuoDirector = -1
                    self.tansuoDeltaX = 0
                elif self.tansuoDeltaX < -2048:
                    self.tansuoDirector = 1
                    self.tansuoDeltaX = 0
        elif Utils.find_and_click(Const.TINGYUAN_TANSUO) == False:
            if Utils.find_and_click(Const.TANSUO_START) == False:
                Utils.find_and_click('./res/tansuo/' + str(25) + '.png')
