import pyautogui
import time 
import sys
import os

import tkinter

sys.path.append("data")
from data import pathInfo

sys.path.append("sources")
from sources import Process
from sources import Interface
from sources import File

_windowSize = Interface.Vector2(200, 200)

def Root() :
    window = SetupWindow("Test")    
    SetUI(window)
    window.mainloop()

def SetupWindow(title : str) -> tkinter.Tk :
    window = Interface.Util.SetWindow(title)
    #Set window Size and Position
    screenWidth, screenHeight = pyautogui.size()
    Interface.Util.SetWindowSizePosition(window, _windowSize, Interface.Vector2(screenWidth / 2, screenHeight / 2))
    
    #Set window transparent
    #window.attributes("-topmost", True)
    window.attributes("-alpha", 0.3)
    window.attributes("-transparentcolor", "white")
    window.configure(background="white")
    return window

def SetUI(window) :
    Interface.Util.AddLabel("title", window, "titleTest")
    Interface.Util.AddButton("restart", window, "restart", func.Restart)
    Interface.Util.AddButton("close", window, "close", func.Close)
    Interface.Util.AddImage("image", window, Interface.Vector2(50,50), "data/image/icon.png")

class func :
    def Restart() :
        python = sys.executable
        os.execl(python, python, * sys.argv)
    def Close(window : tkinter.Tk) :
        Interface.Util.CloseWindow(window)

if (__name__ == "__main__") :
    Root()