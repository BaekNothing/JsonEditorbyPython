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
jsonFrame = None
infoFrame = None
centerScrollText = None
btmFrame = None 

jsonStr = ""
labelList = []

def Root() :
    global window
    window = SetupWindow("Test")    
    SetUI()
    window.mainloop()


def SetupWindow(title : str) -> tkinter.Tk :
    window = Interface.Util.SetWindow(title)
    screenWidth, screenHeight = pyautogui.size()
    Interface.Util.SetWindowSizePosition(
        window, 
        _windowSize, 
        Interface.Vector2(screenWidth / 2 - _windowSize.x / 2 + 200, 
                        screenHeight / 2 - _windowSize.y / 2))
    window.resizable(False, False)
    window.configure(background="white")
    return window

def RenderTopFrame(_windowSize : Interface.Vector2, window : tkinter.Tk) :
    global topFrame
    topFrame = Interface.Util.AddFrame("topFrame", window, Interface.Vector2(640, 50), Interface.Vector2(0, 0))
    topFrame.grid(row=0, column=0, sticky=tkinter.NSEW)

    Interface.Util.AddLabel("title", topFrame, "titleTest").pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("restart", topFrame, "restart", func.Restart).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("close", topFrame, "close", func.Close).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("loadJson", topFrame, "loadJson", lambda : {func.LoadJsonFile(centerScrollText)}).pack(
        side=tkinter.LEFT)
    Interface.Util.AddButton("saveJson", topFrame, "saveJson", lambda : func.SaveJsonFile()).pack(
        side=tkinter.LEFT)
    Interface.Util.AddImage("image", topFrame, Interface.Vector2(50, 50), "data/image/icon.png").pack(
        side=tkinter.LEFT)
    topFrame.place(x=0, y=0, width=_windowSize.x, height=50)

def RenderJsonFrame(_windowSize : Interface.Vector2, window : tkinter.Tk) :   
    global jsonFrame
    global centerScrollText

    scrollWidth = 15

    jsonFrame = Interface.Util.AddFrame(
                    "jsonFrame", 
                    window, 
                    Interface.Vector2(_windowSize.x / 2, _windowSize.y), 
                    Interface.Vector2(0, 100))
    
    center_VerticalScroll = Interface.Util.AddScrollBar(
                                "centerScroll", 
                                jsonFrame, 
                                Interface.Vector2(scrollWidth, _windowSize.y),
                                Interface.Vector2(0, 0), tkinter.VERTICAL)
    
    center_HorizontalScroll = Interface.Util.AddScrollBar(
                                "center_HorizontalScroll", 
                                jsonFrame, 
                                Interface.Vector2(_windowSize.x / 2, scrollWidth), 
                                Interface.Vector2(0, 0), tkinter.HORIZONTAL)

    centerScrollText = Interface.Util.AddText(
                        "centerScrollText", 
                        jsonFrame, 
                        Interface.Vector2(320, 100), 
                        Interface.Vector2(0, 0), 
                        center_VerticalScroll, 
                        center_HorizontalScroll)

    
    jsonFrame.place(x=0, y=50, width=_windowSize.x / 2, height=_windowSize.y - 50)
    centerScrollText.place(x=0, y=0, width=_windowSize.x /
                           2 - scrollWidth, height=_windowSize.y - (50 + scrollWidth))
    center_VerticalScroll.place(
        x=_windowSize.x / 2 - scrollWidth, y=0, width=scrollWidth, height=_windowSize.y - 50)
    center_HorizontalScroll.place(
        x=0, y=_windowSize.y - (50 + scrollWidth), width=_windowSize.x / 2 - scrollWidth, height=scrollWidth)

    jsonFrame.config(background="gray")
    centerScrollText.config(background="lightgray")
    centerScrollText.configure(state=tkinter.DISABLED)

def RenderInfoFrame(_windowSize : Interface.Vector2, window : tkinter.Tk) : 
    global infoFrame
    
    scrollWidth = 15

    infoFrame = Interface.Util.AddFrame(
        "infoFrame",
        window,
        Interface.Vector2(_windowSize.x / 2, 390),
        Interface.Vector2(_windowSize.x / 2, 0))
    info_verticalScroll = Interface.Util.AddScrollBar(
        "info_verticalScroll",
        infoFrame,
        Interface.Vector2(scrollWidth, 0),
        Interface.Vector2(0, 0),
        tkinter.VERTICAL)
    info_horizontalScroll = Interface.Util.AddScrollBar(
        "info_horizontalScroll",
        infoFrame,
        Interface.Vector2(0, scrollWidth),
        Interface.Vector2(0, 0),
        tkinter.HORIZONTAL)
    infoScrollText = Interface.Util.AddText(
        "infoScrollText",
        infoFrame,
        Interface.Vector2(640, 390),
        Interface.Vector2(0, 0),
        info_verticalScroll,
        info_horizontalScroll)

    infoFrame.place(x=_windowSize.x / 2, y=50, width=_windowSize.x / 2, height=_windowSize.y - 50)
    infoScrollText.place(x=0, y=0,  width=_windowSize.x / 2 - scrollWidth, height=_windowSize.y - (50 + scrollWidth))
    info_verticalScroll.place(x=_windowSize.x / 2 - scrollWidth, y=0, width=scrollWidth, height=_windowSize.y - 50)
    info_horizontalScroll.place(x=0, y=_windowSize.y - (50 + scrollWidth), width=_windowSize.x / 2 - scrollWidth, height=scrollWidth)

    infoFrame.config(background="gray")
    infoScrollText.config(background="lightyellow")
    infoScrollText.configure(state=tkinter.DISABLED)

    textInfo = tkinter.StringVar()
    textInfo.set("infoLabel")
    Interface.Util.MakeNewLableInText(infoScrollText, 0, textInfo)

def SetUI() :
    global _windowSize
    global window
    global topFrame

    global btmFrame
    global jsonStr
    
    RenderTopFrame(_windowSize, window)
    RenderJsonFrame(_windowSize, window)
    RenderInfoFrame(_windowSize, window)
    
    
class func :
    def LoadJsonFile(Text: tkinter.Text):
        global jsonStr
        global labelList

        jsonFile = File.ShowFileDialog()
        if (jsonFile != None) :
            jsonStr = JsonParser.MakeJsonToString(
                JsonParser.SetJsonDataFromFile(jsonFile))
            splitedStr = jsonStr.split("\n")
            Interface.Util.AddLabelToTextByLine(Text, 0, splitedStr, labelList)

    def LabellistToString(labelList : list) -> str :
        str = ""
        for obj in labelList :
            if type(obj) is tkinter.Label :
                str += obj.cget("text")
            elif type(obj) is tkinter.Entry :
                str += obj.get()
        return str
    
    def SaveJsonFile() :
        global labelList
        global jsonStr
        global centerScrollText

        newjsonStr = func.LabellistToString(labelList).replace(" ", "")
        if (JsonParser.CheckJsonAble(newjsonStr)) :
            newJsonObject = JsonParser.ValueToJson(newjsonStr)
            newjsonStr = JsonParser.MakeJsonToString(newJsonObject)
            targetFile = File.ShowSaveFileDialog()
            if (targetFile != None) :
                targetFile.write(newjsonStr)
                targetFile.close()
        else :
            print(newjsonStr, "is not json format")
            func.AddLabelToTextByLine(centerScrollText, 0, jsonStr.split("\n"))
            return

    def Restart() :
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    def Close() :
        global window
        Interface.Util.CloseWindow(window)

if (__name__ == "__main__") :
    Root()