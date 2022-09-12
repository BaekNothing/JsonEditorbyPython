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
jsonText = None

infoFrame = None
infoAbleString = None
infoFilePathString = None
infoLogString = None

btmFrame = None 

jsonStr = ""
labelList = []

def Root() :
    global window
    window = SetupWindow("Simple Json Parser v1.0 - by.BAEK")    
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
    
    padxValue = 5

    Interface.Util.AddButton("close", topFrame, "close", func.Close).pack(
        side=tkinter.RIGHT, padx=padxValue)
    Interface.Util.AddButton("restart", topFrame, "restart", func.Restart).pack(
        side=tkinter.RIGHT, padx=padxValue)
    
        
    Interface.Util.AddImage("image", topFrame, Interface.Vector2(50, 50), "./data/icon.png").pack(
        side=tkinter.LEFT, padx=padxValue)
    Interface.Util.AddButton("loadJson", topFrame, "loadJson", lambda : {func.LoadJsonFile(jsonText)}).pack(
        side=tkinter.LEFT, padx=padxValue)
    Interface.Util.AddButton("reset", topFrame, "reset", func.Reset).pack(
        side=tkinter.LEFT, padx=padxValue)
    Interface.Util.AddButton("saveJson", topFrame, "saveJson", lambda : func.SaveJsonFile()).pack(
        side=tkinter.LEFT, padx=padxValue)
    Interface.Util.AddButton("saveNewFile", topFrame, "saveNewFile", lambda : func.SaveNewFile()).pack(
        side=tkinter.LEFT, padx=padxValue)
    topFrame.place(x=0, y=0, width=_windowSize.x, height=50)

def RenderJsonFrame(_windowSize : Interface.Vector2, window : tkinter.Tk) :   
    global jsonFrame
    global jsonText

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

    jsonText = Interface.Util.AddText(
                        "jsonText", 
                        jsonFrame, 
                        Interface.Vector2(320, 100), 
                        Interface.Vector2(0, 0), 
                        center_VerticalScroll, 
                        center_HorizontalScroll)

    
    jsonFrame.place(x=0, y=50, width=_windowSize.x / 2, height=_windowSize.y - 50)
    jsonText.place(x=0, y=0, width=_windowSize.x /
                           2 - scrollWidth, height=_windowSize.y - (50 + scrollWidth))
    center_VerticalScroll.place(
        x=_windowSize.x / 2 - scrollWidth, y=0, width=scrollWidth, height=_windowSize.y - 50)
    center_HorizontalScroll.place(
        x=0, y=_windowSize.y - (50 + scrollWidth), width=_windowSize.x / 2 - scrollWidth, height=scrollWidth)

    jsonFrame.config(background="gray")
    jsonText.config(background="lightgray")
    jsonText.configure(state=tkinter.DISABLED)

def RenderInfoFrame(_windowSize : Interface.Vector2, window : tkinter.Tk) : 
    global infoFrame
    global infoAbleString
    global infoFilePathString
    global infoLogString

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
    infoScrollText.config(background="white")

    infoScrollText.insert(tkinter.END, "\n")
    infoAbleString = tkinter.StringVar()
    infoAbleString.set("Check results convertible to json : True")
    Interface.Util.MakeNewLableInText(infoScrollText, infoAbleString).config(
        background="white")
    infoScrollText.insert(tkinter.END, "\n")
    infoFilePathString = tkinter.StringVar()
    infoFilePathString.set("File path : ")
    Interface.Util.MakeNewLableInText(infoScrollText, infoFilePathString).config(
        background="white")
    infoScrollText.insert(tkinter.END, "\n")
    infoLogString = tkinter.StringVar()
    infoLogString.set("Log : ")
    Interface.Util.MakeNewLableInText(infoScrollText, infoLogString).config(
        background="white")

    infoScrollText.configure(state=tkinter.DISABLED)

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
        global infoFilePathString

        jsonFile = File.ShowFileDialog()
        if (jsonFile != None and jsonFile != "") :
            infoFilePathString.set("File path : " + jsonFile)
            jsonStr = JsonParser.MakeJsonToString(
                JsonParser.SetJsonDataFromFile(jsonFile))
            splitedStr = jsonStr.split("\n")
            Interface.Util.AddLabelToTextByLine(Text, splitedStr, labelList, func.EntryAction)
        else :
            infoFilePathString.set("File path : ")

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
        global jsonText
        global infoFilePathString
        global infoLogString

        if(jsonStr == "") : return

        newjsonStr = func.LabellistToString(labelList).replace(" ", "")
        if (JsonParser.CheckJsonAble(newjsonStr)) :
            newJsonObject = JsonParser.ValueToJson(newjsonStr)
            newjsonStr = JsonParser.MakeJsonToString(newJsonObject)
            File.SaveFile(infoFilePathString.get().replace("File path : ", ""), newjsonStr)
            infoLogString.set("Log : Save Success")
        else :
            infoLogString.set("Log : Save Fail, Check Json Format")
            Interface.Util.AddLabelToTextByLine(jsonText, jsonStr.split("\n"), labelList, func.EntryAction)
            return

    def SaveNewFile() : 
        global labelList
        global jsonStr
        global jsonText
        global infoLogString
        
        if(jsonStr == "") : return

        newjsonStr = func.LabellistToString(labelList).replace(" ", "")
        if (JsonParser.CheckJsonAble(newjsonStr)) :
            newJsonObject = JsonParser.ValueToJson(newjsonStr)
            newjsonStr = JsonParser.MakeJsonToString(newJsonObject)
            targetFile = File.ShowSaveFileDialog()
            if (targetFile != None) :
                targetFile.write(newjsonStr)
                targetFile.close()
                infoLogString.set("Log : New file Saved")
        else :
            infoLogString.set("Log : Save Fail, Check Json Format")
            Interface.Util.AddLabelToTextByLine(jsonText, jsonStr.split("\n"), labelList, func.EntryAction)
            return

    def EntryAction(var : tkinter.StringVar) :
        global infoAbleString
        global labelList
        if(JsonParser.CheckJsonAble(func.LabellistToString(labelList).replace(" ", ""))) :
            infoAbleString.set("Check results convertible to json : True")
        else :
            infoAbleString.set("Check results convertible to json : False")

    def Reset() : 
        global jsonStr
        global jsonText
        global labelList
        global infoLogString

        if(jsonStr == "") : return
        if(Interface.Util.ShowYesNoDialog("Reset", "Are you sure you want to reset?")) :
            Interface.Util.AddLabelToTextByLine(jsonText, jsonStr.split("\n"), labelList, func.EntryAction)
            infoLogString.set("Log : Reset Complete")

    def Restart() :
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    def Close() :
        global window
        Interface.Util.CloseWindow(window)

if (__name__ == "__main__") :
    try:
        os.chdir(sys._MEIPASS)
        print(sys._MEIPASS)
    except:
        os.chdir(os.getcwd())
    Root()