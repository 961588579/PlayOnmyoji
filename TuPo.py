#!/usr/bin/env python

import time

import Const
import Utils


class TuPo:

    def __init__(self):
        pass

    def doTuPo(self):
        if Utils.find_and_click(Const.TUPO_ATTACK):
            return
        # 选择阴阳寮突破
        if Utils.find_and_click(Const.TUPO_LIAO):
            pass
        # 挑战没有挑战过的玩家
        if Utils.find_and_click(Const.TUPO_NEW):
            return
        # 如果没有未挑战过的玩家，则挑战之前挑战失败的玩家
        elif Utils.find_and_click(Const.TUPO_FAILED):
            return
        # 进入结界突破
        if Utils.find_and_click(Const.TUPO_ENTER):
            return
        if Utils.find_and_click(Const.TINGYUAN_TANSUO):
            return
        if Utils.find_and_click(Const.COMMON_PREPARE):
            return
