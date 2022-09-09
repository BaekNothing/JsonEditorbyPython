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
centerScroll = None
centerCanvas = None
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
    global centerScroll
    global centerCanvas
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
    centerFrame.pack(side=tkinter.TOP)

    centerScroll = Interface.Util.AddScrollBar('centerScroll', centerFrame, Interface.Vector2(30, 380), Interface.Vector2(0, 0), 'vertical')
    centerScroll.pack(side=tkinter.LEFT, fill=tkinter.Y)
    centerCanvas = Interface.Util.AddCanvas('centerCanvas', centerFrame, Interface.Vector2(320, 380), Interface.Vector2(0, 0))
    centerCanvas.pack(side=tkinter.LEFT)
    centerCanvas.configure(scrollregion=centerCanvas.bbox("all"))
    centerCanvas.configure(yscrollcommand=centerScroll.set)    

    centerScroll.config(command=centerCanvas.yview)
    
    
    func.JsonToLables(
        centerCanvas,
        JsonParser.SetJsonDataFromFile("./tests/test.json"),
        0,0)

    # btmFrame = Interface.Util.AddFrame("frameBtm", window, Interface.Vector2(640, 100), Interface.Vector2(0, 380))
    # btmFrame.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=False)
    # Interface.Util.AddLabel("btmLabel", btmFrame, "btmLabelTest").pack(side=tkinter.LEFT)

class func :
    def LoadJsonFile() :
        global centerCanvas
        jsonFile = File.ShowFileDialog()
        if (jsonFile != None) :
            jsonObject=  JsonParser.SetJsonDataFromFile(jsonFile)
            height = func.JsonToLables(centerCanvas, jsonObject, 0, 0)
            #resize centerCanvas
            centerCanvas.configure(scrollregion=centerCanvas.bbox("all"))
            centerCanvas.config(height=height * 20)
            

    #make dict to Labels 
    #like this : 
    # key : value
    # key : [list]
    # key : {
    #  key : value}

    def JsonToLables(window : tkinter.Canvas, jObject : json, row : numbers, column : numbers) -> numbers:
        for key in jObject.keys() :
            if (isinstance(jObject[key], dict)) :
                Interface.Util.AddLabel(key, window, key).grid(row=row, column=column)
                row += 1
                row = func.JsonToLables(window, jObject[key], row, column + 1)
            elif (isinstance(jObject[key], list)) :
                Interface.Util.AddLabel(key, window, key).grid(row=row, column=column)
                row += 1
                for value in jObject[key] :
                    if (isinstance(value, dict)) :
                        row = func.JsonToLables(window, value, row, column + 1)
                    else :
                        Interface.Util.AddLabel(key, window, value).grid(row=row, column=column + 1)
                        row += 1
            else :
                Interface.Util.AddLabel(key, window, key).grid(row=row, column=column)
                Interface.Util.AddLabel(key, window, jObject[key]).grid(row=row, column=column + 1)
                row += 1
        return row

    def Restart() :
        python = sys.executable
        os.execl(python, python, * sys.argv)
    def Close() :
        global window
        Interface.Util.CloseWindow(window)

if (__name__ == "__main__") :
    Root()