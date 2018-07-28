
import tkinter as tk
from tkinter import messagebox as mBox
from tkinter import Menu, Spinbox, scrolledtext, ttk

import Const
import Utils
from PlayManager import PlayManager


pm = PlayManager()
pm.startPlay()

# Modified Button Click Function


def connectDevice():
    Utils.CMD("adb connect " + Const.DEVICE.MUMU)
    Utils.CMD("adb wait-for-device")


def startPlay():
    pm.autoPlay = not pm.autoPlay
    if pm.autoPlay == True:
        connectDevice()
        action.configure(text='停止')
    else:
        action.configure(text='开始')


def changeMode(*args):
    pm.changeMode(modeChosen.current())


if __name__ == '__main__':

    # Create instance
    win = tk.Tk()

    # Add a title
    win.title('不怎么好用阴阳师助手')
    win.resizable(600, 300)

    #---------------Tab1控件介绍------------------#
    # We are creating a container tab3 to hold all other widgets
    monty = ttk.LabelFrame(win, text='')
    monty.grid(column=0, row=0, padx=8, pady=4)

    # Adding a Button
    action = ttk.Button(monty, text="开始", width=10, command=startPlay)
    action.grid(column=2, row=0, rowspan=2, ipady=7)

    ttk.Label(monty, text="请选择游戏模式:").grid(column=1, row=0, sticky='W')

    # Adding a Combobox

    mode = tk.StringVar()
    modeChosen = ttk.Combobox(monty, width=12, textvariable=mode)
    modeChosen['values'] = ('探索', '御魂', '结界突破')
    modeChosen.grid(column=1, row=1)
    modeChosen.current(0)  # 设置初始显示值，值为元组['values']的下标
    modeChosen.config(state='readonly')  # 设为只读模式
    modeChosen.bind("<<ComboboxSelected>>", changeMode)
    # ======================
    # Start GUI
    # ======================
    win.mainloop()
    pass
