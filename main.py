import json
import numbers
from tokenize import Number
import pyautogui
import time 
import sys
import os

import tkinter

sys.path.append("data")
from data import pathInfo

sys.path.append("sources")
from sources import JsonParser
from sources import Interface
from sources import File

_windowSize = Interface.Vector2(640, 490)
window = None
topFrame = None
centerFrame = None
btmFrame = None 

def Root() :
    global window
    window = SetupWindow("Test")    
    SetUI()
    window.mainloop()

def SetupWindow(title : str) -> tkinter.Tk :
    window = Interface.Util.SetWindow(title)
    #Set window Size and Position
    screenWidth, screenHeight = pyautogui.size()
    Interface.Util.SetWindowSizePosition(window, _windowSize, Interface.Vector2(screenWidth / 2 - _windowSize.x / 2, screenHeight / 2 - _windowSize.y / 2))
    
    #Set window transparent
    #window.attributes("-topmost", True)
    #window.attributes("-alpha", 0.3)
    #window.attributes("-transparentcolor", "white")
    window.configure(background="white")
    return window

def SetUI() :
    global window
    global topFrame
    global centerFrame
    global btmFrame

    topFrame = Interface.Util.AddFrame("topFrame", window, Interface.Vector2(640, 100), Interface.Vector2(0, 0))
    topFrame.pack(side=tkinter.TOP, fill=tkinter.X)

    Interface.Util.AddLabel("title", topFrame, "titleTest").pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("restart", topFrame, "restart", func.Restart).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("close", topFrame, "close", func.Close).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("loadJson", topFrame, "loadJson", func.LoadJsonFile).pack(
        side=tkinter.LEFT)
    Interface.Util.AddImage("image", topFrame, Interface.Vector2(50, 50), "data/image/icon.png").pack(
        side=tkinter.LEFT)

    centerFrame = Interface.Util.AddFrame("frameCenter", window, Interface.Vector2(640, 380), Interface.Vector2(0, 0))
    centerFrame.configure(background="green")
    centerFrame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
    Interface.Util.AddLabel("labelCenter", centerFrame, "center").pack(side=tkinter.TOP)

    btmFrame = Interface.Util.AddFrame("frameBtm", window, Interface.Vector2(640, 100), Interface.Vector2(0, 380))
    btmFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=False)
    Interface.Util.AddLabel("btmLabel", btmFrame, "btmLabelTest").pack(side=tkinter.LEFT)

class func :
    def LoadJsonFile() :
        global centerScrollFrame
        jsonFile = File.ShowFileDialog()
        if (jsonFile != None) :
            jsonObject=  JsonParser.SetJsonDataFromFile(jsonFile)
            func.DictToLabels(centerScrollFrame, jsonObject, "", 0)

    def Restart() :
        python = sys.executable
        os.execl(python, python, * sys.argv)
    def Close() :
        global window
        Interface.Util.CloseWindow(window)

if (__name__ == "__main__") :
    Root()