import os

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image, ImageTk

class Vector2:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
    
class Util :    
    def AddButton(name : str, window : tkinter.Tk, text : str, command) -> tkinter.Button :
        return tkinter.Button(window, text=text, command=command)

    def AddLabel(name : str, window : tkinter.Tk, text : str) -> tkinter.Label :
        return tkinter.Label(window, text=text)

    def AddEntry(name : str, window : tkinter.Tk, text : str) -> tkinter.Entry:
        entry = tkinter.Entry(window)
        entry.insert(0, text)
        return entry

    def AddFrame(name : str, window : tkinter.Tk, size : Vector2, position : Vector2) -> tkinter.Frame:
        frame = tkinter.Frame(window)
        frame.place(x=position.x, y=position.y, width=size.x, height=size.y)
        return frame

    def AddScrollBar(name : str, window : tkinter.Tk, size : Vector2, position : Vector2, orient : str) -> tkinter.Scrollbar:
        scrollBar = tkinter.Scrollbar(window, orient=orient)
        scrollBar.place(x=position.x, y=position.y, width=size.x, height=size.y)
        return scrollBar

    def AddText(name : str, window : tkinter.Tk, size : Vector2, position : Vector2, vertical_Scrollbar : tkinter.Scrollbar, horizontal_Scrollbar : tkinter.Scrollbar) -> tkinter.Text:
        text = tkinter.Text(window)
        text.place(x=position.x, y=position.y, width=size.x, height=size.y)
        if(vertical_Scrollbar != None):
            text.config(yscrollcommand=vertical_Scrollbar.set)
            vertical_Scrollbar.config(command=text.yview)
        if(horizontal_Scrollbar != None):
            text.config(xscrollcommand=horizontal_Scrollbar.set)
            horizontal_Scrollbar.config(command=text.xview)
        return text

    def AddImage(name : str, window : tkinter.Tk, size : Vector2, path : str) -> tkinter.Image :
        originImage = Image.open(path)
        resizedImage = originImage.resize((size.x, size.y))
        tkImage = ImageTk.PhotoImage(resizedImage) 
        label = tkinter.Label(window, image=tkImage)
        label.image = tkImage
        label.place(x=0, y=0, width=size.x, height=size.y)
        return label

    def SetWindow(title : str) -> tkinter.Tk:
        window = tkinter.Tk()
        window.title(title)
        window.resizable(True, True)
        Util.__SetWindowIcon(window, "data/image/favicon.ico")
        return window

    def CloseWindow(window : tkinter.Tk) -> None:
        window.destroy()
    
    def __SetWindowIcon(window : tkinter.Tk, icon : os.__file__):
        window.iconbitmap(icon)

    def SetWindowSizePosition(window : tkinter.Tk, size : Vector2, position : Vector2) :
        window.geometry(f"{size.x}x{size.y}+{('%.0f'%position.x)}+{'%.0f'%position.y}")

    # Make Json to Labels in Text
    def AddLabelToTextByLine(Text: tkinter.Text, line : int, jsonStr : list, labelList : list) :
        Text.delete("1.0", tkinter.END)
        labelList.clear()
        for eachLine in jsonStr : 
            Util.EachLineToTkinterObject(Text, line, eachLine, labelList)
            line += 1
        Text.configure(state=tkinter.DISABLED)
        
    def EachLineToTkinterObject(Text: tkinter.Text, line : int, eachLine : str, labelList : list):
        if (eachLine.__contains__(":")) :
            if (eachLine.__contains__("{") or eachLine.__contains__("[")) :
                labelList.append(Util.MakeNewLableInText(Text, line, eachLine))
                Text.insert(tkinter.END, "\n")
            else :
                key, value = eachLine.split(":")
                labelList.append(Util.MakeNewLableInText(Text, line, key + ":"))
                labelList.append(Util.MakeNewEntryInText(Text, line, value))
                Text.insert(tkinter.END, "\n")
        else : 
            if (eachLine.__contains__("{") or eachLine.__contains__("}") or 
                eachLine.__contains__("[") or eachLine.__contains__("]")) :
                labelList.append(Util.MakeNewLableInText(Text, line, eachLine))
                Text.insert(tkinter.END, "\n")
            else :
                labelList.append(Util.MakeNewEntryInText(Text, line, eachLine))
                Text.insert(tkinter.END, "\n")

    def MakeNewLableInText(Text: tkinter.Text, line : int, eachLine : str) -> tkinter.Label:
        newLabel = Util.AddLabel("label" + str(line), Text, eachLine)
        newLabel.pack(side=tkinter.TOP, fill=tkinter.X)
        Text.configure(state="normal")
        Text.window_create(tkinter.END, window=newLabel)
        return newLabel

    def MakeNewEntryInText(Text: tkinter.Text, line : int, eachLine : str) -> tkinter.Entry:
        newEntry = Util.AddEntry("entry" + str(line), Text, eachLine)
        newEntry.pack(side=tkinter.TOP, fill=tkinter.X)
        Text.configure(state="normal")
        Text.window_create(tkinter.END, window=newEntry)
        return newEntry
