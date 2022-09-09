import json
import sys
import os
import tkinter

import pyautogui

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
centerScroll = None
centerScrollText = None
btmFrame = None 

jsonStr = ""

def Root() :
    global window
    window = SetupWindow("Test")    
    SetUI()
    window.mainloop()

def SetupWindow(title : str) -> tkinter.Tk :
    window = Interface.Util.SetWindow(title)
    #Set window Size and Position
    screenWidth, screenHeight = pyautogui.size()
    Interface.Util.SetWindowSizePosition(window, _windowSize, Interface.Vector2(screenWidth / 2 - _windowSize.x / 2 + 200, screenHeight / 2 - _windowSize.y / 2))
    window.resizable(False, False)
    #Set window transparent
    #window.attributes("-topmost", True)
    #window.attributes("-alpha", 0.3)
    #window.attributes("-transparentcolor", "white")
    window.configure(background="white")
    return window

def SetUI() :
    global window
    global topFrame
    global centerScroll
    global centerScrollText
    global btmFrame
    global jsonStr

    topFrame = Interface.Util.AddFrame("topFrame", window, Interface.Vector2(640, 100), Interface.Vector2(0, 0))
    topFrame.pack(side=tkinter.TOP, fill=tkinter.X)

    Interface.Util.AddLabel("title", topFrame, "titleTest").pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("restart", topFrame, "restart", func.Restart).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("close", topFrame, "close", func.Close).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("loadJson", topFrame, "loadJson", lambda : {func.LoadJsonFile(centerScrollText)}).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("saveJson", topFrame, "saveJson", lambda : func.SaveJsonFile(jsonStr)).pack(
        side=tkinter.LEFT)
    Interface.Util.AddImage("image", topFrame, Interface.Vector2(50, 50), "data/image/icon.png").pack(
        side=tkinter.LEFT)

    centerFrame = Interface.Util.AddFrame("centerFrame", window, Interface.Vector2(640, 390), Interface.Vector2(0, 100))
    centerFrame.pack(side=tkinter.TOP, fill=tkinter.X)

    centerScroll = Interface.Util.AddScrollBar("centerScroll", centerFrame, Interface.Vector2(640, 390), Interface.Vector2(0, 0), tkinter.VERTICAL)
    centerScroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    centerScrollText = Interface.Util.AddText("centerScrollText", centerFrame, Interface.Vector2(640, 390), Interface.Vector2(0, 0), centerScroll)
    centerScrollText.pack(side=tkinter.TOP, fill=tkinter.X)

    #centerScrollText.configure(state="disabled")


class func :
    def LoadJsonFile(Text: tkinter.Text):
        global jsonStr
        jsonFile = File.ShowFileDialog()
        if (jsonFile != None) :
            jsonStr = JsonParser.MakeJsonToString(
                JsonParser.SetJsonDataFromFile(jsonFile))
            Text.configure(state="normal")
            Text.delete("1.0", tkinter.END)
            Text.insert(tkinter.END, jsonStr)
            Text.configure(state="disabled")
    
    def SaveJsonFile(jsonStr : str) :
        jsonStr = jsonStr.replace("\'", "\"")
        targetFile = File.ShowSaveFileDialog()
        if (targetFile != None) :
            targetFile.write(jsonStr)
            targetFile.close()

    def Restart() :
        python = sys.executable
        os.execl(python, python, * sys.argv)
    def Close() :
        global window
        Interface.Util.CloseWindow(window)

if (__name__ == "__main__") :
    Root()