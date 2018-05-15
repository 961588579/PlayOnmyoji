#!/usr/bin/env python

import time
import Utils


class TanSuo:

    def __init__(self):
        # 用来记录探索时拖动的方向 1 手指从右向左   -1 手指从左向右
        self.tansuoDirector = 1
        # 用来记录探索时拖动的偏移，范围在-2048~2048
        self.tansuoDeltaX = 0

    def doEnterTanSuo(self, level):
        if Utils.find_and_click('./res/tansuo/start.png') == False:
            Utils.find_and_click('./res/tansuo/' + str(level) + '.png')

    def doTanSuo(self):

        # 探索Boss
        print("寻找boss")

        if Utils.find_and_click('./res/tansuo/boss32x32.png') == False:
            # 探索小怪
            print("没有boss，寻找小怪")

            if Utils.find_and_click('./res/tansuo/enemy.png') == False:

                if Utils.find_and_click('./res/tansuo/reward.png') == False:

                    pos = Utils.find('./res/tansuo/getreward.png')
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
