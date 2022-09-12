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
        if(type(text) == tkinter.StringVar):
            return tkinter.Label(window, textvariable=text)
        else :
            return tkinter.Label(window, text=text)

    def AddEntry(name : str, window : tkinter.Tk, text : str) -> tkinter.Entry:
        entry = tkinter.Entry(window)
        if(type(text) == tkinter.StringVar):
            entry.config(textvariable=text)
        else :
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
        Util.SetIcon(
            window,
            './data/favicon.ico'
        )
        return window

    def SetIcon(window : tkinter.Tk, path : str) -> None:
        window.iconbitmap(path)

    def CloseWindow(window : tkinter.Tk) -> None:
        window.destroy()

    def SetWindowSizePosition(window : tkinter.Tk, size : Vector2, position : Vector2) :
        window.geometry(f"{size.x}x{size.y}+{('%.0f'%position.x)}+{'%.0f'%position.y}")

    # Make Json to Labels in Text
    def AddLabelToTextByLine(Text: tkinter.Text, jsonStr : list, labelList : list, action) :
        #disable focus in labelList
        for label in labelList:
            label.config(state="disabled")
            label.destroy()
        labelList.clear()

        Text.configure(state="normal")
        Text.delete("1.0", tkinter.END)

        for eachLine in jsonStr : 
            Util.EachLineToTkinterObject(Text, eachLine, labelList, action)
        Text.configure(state=tkinter.DISABLED)
        
    def EachLineToTkinterObject(Text: tkinter.Text, eachLine : str, labelList : list, action):
        if (eachLine.__contains__(":")) :
            if (eachLine.__contains__("{") or eachLine.__contains__("[")) :
                labelList.append(Util.MakeNewLableInText(Text, eachLine))
                Text.insert(tkinter.END, "\n")
            else :
                key, value = eachLine.split(":")
                labelList.append(Util.MakeNewLableInText(Text, key + ":"))
                labelList.append(Util.MakeNewEntryInText(Text, value, action))
                Text.insert(tkinter.END, "\n")
        else : 
            if (eachLine.__contains__("{") or eachLine.__contains__("}") or 
                eachLine.__contains__("[") or eachLine.__contains__("]")) :
                labelList.append(Util.MakeNewLableInText(Text, eachLine))
                Text.insert(tkinter.END, "\n")
            else :
                labelList.append(Util.MakeNewEntryInText(Text, eachLine, action))
                Text.insert(tkinter.END, "\n")

    def MakeNewLableInText(Text: tkinter.Text, eachLine : str) -> tkinter.Label:
        newLabel = Util.AddLabel("label", Text, eachLine)
        newLabel.pack(side=tkinter.TOP, fill=tkinter.X)
        Text.configure(state="normal")
        Text.window_create(tkinter.END, window=newLabel)
        return newLabel

    def MakeNewEntryInText(Text: tkinter.Text, eachLine : str, action) -> tkinter.Entry:
        entryString = tkinter.StringVar()
        entryString.set(eachLine)
        entryString.trace("w", lambda name, index, mode, entryString=entryString, action=action: action(entryString))
        newEntry = Util.AddEntry("entry", Text, entryString)
        newEntry.pack(side=tkinter.TOP, fill=tkinter.X)
        Text.configure(state="normal")
        Text.window_create(tkinter.END, window=newEntry)
        return newEntry

    def ShowYesNoDialog(title : str, message : str) -> bool:
        return messagebox.askyesno(title, message)