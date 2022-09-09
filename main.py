from distutils.log import info
import json
import sys
import os
import tkinter
from turtle import width
from matplotlib.hatch import VerticalHatch

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
    #Set window transparent
    #window.attributes("-topmost", True)
    #window.attributes("-alpha", 0.3)
    #window.attributes("-transparentcolor", "white")
    window.configure(background="white")
    return window

def RenderTopFrame() :
    global _windowSize
    global window
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

def RenderJsonFrame() :
    global _windowSize
    global window
    
    global jsonFrame
    global centerScrollText

    jsonFrame = Interface.Util.AddFrame(
                    "jsonFrame", 
                    window, 
                    Interface.Vector2(_windowSize.x / 2, _windowSize.y), 
                    Interface.Vector2(0, 100))
    
    center_VerticalScroll = Interface.Util.AddScrollBar(
                                "centerScroll", 
                                jsonFrame, 
                                Interface.Vector2(10, _windowSize.y), 
                                Interface.Vector2(0, 0), tkinter.VERTICAL)
    
    center_HorizontalScroll = Interface.Util.AddScrollBar(
                                "center_HorizontalScroll", 
                                jsonFrame, 
                                Interface.Vector2(_windowSize.x / 2, 10), 
                                Interface.Vector2(0, 0), tkinter.HORIZONTAL)

    centerScrollText = Interface.Util.AddText(
                        "centerScrollText", 
                        jsonFrame, 
                        Interface.Vector2(320, 100), 
                        Interface.Vector2(0, 0), 
                        center_VerticalScroll, 
                        center_HorizontalScroll)

    
    jsonFrame.place(x=0, y=50, width=_windowSize.x / 2, height=_windowSize.y - 50)
    centerScrollText.place(x=0, y=0, width=_windowSize.x / 2 - 10, height=_windowSize.y - 60)
    center_VerticalScroll.place(x=_windowSize.x / 2 - 10, y=0, width=10, height=_windowSize.y - 50)
    center_HorizontalScroll.place(x=0, y=_windowSize.y - 60, width=_windowSize.x / 2 - 10, height=10)

    jsonFrame.config(background="gray")
    centerScrollText.config(background="lightgray")
    centerScrollText.configure(state=tkinter.DISABLED)

def SetUI() :
    global _windowSize
    global window
    
    global infoFrame
    
    global btmFrame
    global jsonStr
    
    RenderTopFrame()
    RenderJsonFrame()    
    
    infoFrame = Interface.Util.AddFrame(
                    "infoFrame", 
                    window, 
                    Interface.Vector2(_windowSize.x / 2, 390), 
                    Interface.Vector2(_windowSize.x / 2, 0))
    
    info_verticalScroll = Interface.Util.AddScrollBar(
                            "info_verticalScroll",
                            infoFrame,
                            Interface.Vector2(10, 0),
                            Interface.Vector2(0, 0),
                            tkinter.VERTICAL)
    info_horizontalScroll = Interface.Util.AddScrollBar(
                            "info_horizontalScroll",
                            infoFrame,
                            Interface.Vector2(0, 10),
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
    infoScrollText.place(x=_windowSize.x / 2, y=0, width=_windowSize.x / 2 - 10, height=_windowSize.y - 60)
    info_verticalScroll.place(x=_windowSize.x - 10, y=0, width=10, height=_windowSize.y - 50)
    info_horizontalScroll.place(x=_windowSize.x / 2, y=_windowSize.y - 60, width=_windowSize.x / 2 - 10, height=10)

    infoFrame.config(background="gray")
    infoScrollText.config(background="lightyellow")
    infoScrollText.configure(state=tkinter.DISABLED)
    
class func :
    def LoadJsonFile(Text: tkinter.Text):
        global jsonStr
        jsonFile = File.ShowFileDialog()
        if (jsonFile != None) :
            jsonStr = JsonParser.MakeJsonToString(
                JsonParser.SetJsonDataFromFile(jsonFile))
            splitedStr = jsonStr.split("\n")
            func.AddLabelToTextByLine(Text, 0, splitedStr)

    def AddLabelToTextByLine(Text: tkinter.Text, line : int, jsonStr : list) :
        global labelList
        Text.delete("1.0", tkinter.END)
        labelList.clear()
        for eachLine in jsonStr : 
            func.EachLineToTkinterObject(Text, line, eachLine)
            line += 1
        centerScrollText.configure(state=tkinter.DISABLED)
        
    def EachLineToTkinterObject(Text: tkinter.Text, line : int, eachLine : str):
        if (eachLine.__contains__(":")) :
            if (eachLine.__contains__("{") or eachLine.__contains__("[")) :
                func.MakeNewLableInText(Text, line, eachLine)
                Text.insert(tkinter.END, "\n")
            else :
                key, value = eachLine.split(":")
                func.MakeNewLableInText(Text, line, key + ":")
                func.MakeNewEntryInText(Text, line, value)
                Text.insert(tkinter.END, "\n")
        else : 
            if (eachLine.__contains__("{") or eachLine.__contains__("}") or 
                eachLine.__contains__("[") or eachLine.__contains__("]")) :
                func.MakeNewLableInText(Text, line, eachLine)
                Text.insert(tkinter.END, "\n")
            else :
                func.MakeNewEntryInText(Text, line, eachLine)
                Text.insert(tkinter.END, "\n")
            

    def MakeNewLableInText(Text: tkinter.Text, line : int, eachLine : str):
        global labelList
        newLabel = Interface.Util.AddLabel("label" + str(line), Text, eachLine)
        newLabel.pack(side=tkinter.TOP, fill=tkinter.X)
        labelList.append(newLabel)
        Text.configure(state="normal")
        Text.window_create(tkinter.END, window=newLabel)

    def MakeNewEntryInText(Text: tkinter.Text, line : int, eachLine : str) :
        global labelList
        newEntry = Interface.Util.AddEntry("entry" + str(line), Text, eachLine)
        newEntry.pack(side=tkinter.TOP, fill=tkinter.X)
        labelList.append(newEntry)
        Text.configure(state="normal")
        Text.window_create(tkinter.END, window=newEntry)

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
        try :
            newJsonObject = json.loads(newjsonStr)
        except ValueError as e :
            print(newjsonStr, "is not json format")
            func.AddLabelToTextByLine(centerScrollText, 0, jsonStr.split("\n"))
            return
        newjsonStr = JsonParser.MakeJsonToString(newJsonObject)
        targetFile = File.ShowSaveFileDialog()
        if (targetFile != None) :
            targetFile.write(newjsonStr)
            targetFile.close()

    def Restart() :
        python = sys.executable
        os.execl(python, python, * sys.argv)
    def Close() :
        global window
        Interface.Util.CloseWindow(window)

if (__name__ == "__main__") :
    Root()