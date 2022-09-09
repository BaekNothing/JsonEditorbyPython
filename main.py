from cProfile import label
from cgitb import text
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
labelList = []

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
    Interface.Util.AddButton("saveJson", topFrame, "saveJson", lambda : func.SaveJsonFile()).pack(
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
            splitedStr = jsonStr.split("\n")
            func.AddLabelToTextByLine(Text, 0, splitedStr)

    def AddLabelToTextByLine(Text: tkinter.Text, line : int, jsonStr : list) :
        global labelList
        Text.delete("1.0", tkinter.END)
        labelList.clear()
        for eachLine in jsonStr : 
            func.EachLineToTkinterObject(Text, line, eachLine)
            line += 1
        
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
            str += "\n"
        return str
    
    def SaveJsonFile() :
        global labelList
        global jsonStr
        global centerScrollText

        newjsonStr = func.LabellistToString(labelList).replace(" ", "")
        try :
            json.loads(newjsonStr)
        except ValueError as e :
            print(newjsonStr, "is not json format")
            func.AddLabelToTextByLine(centerScrollText, 0, jsonStr.split("\n"))
            return
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