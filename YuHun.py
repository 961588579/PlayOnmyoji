#!/usr/bin/env python

import time

import Const
import Utils

MODE_TIAOZHAN = 0
MODE_ZUDUI = 1


class YuHun:

    def __init__(self):
        self.mode = MODE_TIAOZHAN
        pass

    def doYuHun(self):
        if self.mode == MODE_TIAOZHAN:
            self.doTiaoZhan()
        elif self.mode == MODE_ZUDUI:
            self.doZuDui()

    def doTiaoZhan(self):

        if Utils.find_and_click(Const.YUHUN_HUN10):
            if Utils.find_and_click(Const.COMMON_ZHEN_RONG_SUO_DING):
                return
            if Utils.find_and_click(Const.COMMON_TIAO_ZHAN):
                return
            return
        if Utils.find_and_click(Const.YUHUN_DASHE):
            return
        if Utils.find_and_click(Const.YUHUN_ENTER):
            return
        if Utils.find_and_click(Const.TINGYUAN_TANSUO):
            return
        if Utils.find_and_click(Const.COMMON_PREPARE):
            return

    def doZuDui(self):

        if Utils.find_and_click(Const.COMMON_DEFAULT_INVENT):
            return
        if Utils.find_and_click(Const.COMMON_YES):
            return
        if Utils.find_and_click(Const.COMMON_PREPARE):
            return
        if Utils.find_and_click(Const.COMMON_FIGHT):
            return
        if Utils.find_and_click(Const.COMMON_CREATE):
            return
        if Utils.find_and_click(Const.COMMON_CREATETEAM):
            return
        if Utils.find_and_click(Const.COMMON_ZUDUI):
            return
        if Utils.find_and_click(Const.YUHUN_HUN10):
            return
        if Utils.find_and_click(Const.COMMON_FIGHT):
            return
        if Utils.find_and_click(Const.YUHUN_DASHE):
            return
        if Utils.find_and_click(Const.YUHUN_ENTER):
            return
        if Utils.find_and_click(Const.TINGYUAN_TANSUO):
            return
