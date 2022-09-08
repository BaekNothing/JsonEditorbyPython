import os

import tkinter
import tkinter.messagebox
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.font
import tkinter.ttk
import tkinter.scrolledtext
import unittest

from PIL import Image, ImageTk

class Vector2:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
    
class Util :    
    __btnList = {str : tkinter.Button}
    def AddButton(name : str, root : tkinter.Tk, text : str, command) -> tkinter.Button :
        Util.__btnList[name] = Util.__SetButtonInWindow(root, text, command)
        return Util.__btnList[name]

    def GetButton(name) -> tkinter.Button :
        return Util.__btnList[name]

    __lblList = {str : tkinter.Label}
    def AddLabel(name : str, root : tkinter.Tk, text : str) -> tkinter.Label :
        Util.__lblList[name] = Util.__SetLabelInWindow(root, text)
        return Util.__lblList[name]

    def GetLabel(name) -> tkinter.Label :
        return Util.__lblList[name]

    __entryList = {str : tkinter.Entry}
    def AddEntry(name : str, root : tkinter.Tk, text : str) -> tkinter.Entry:
        Util.__entryList[name] = Util.__SetEntryInWindow(root, text)
        return Util.__entryList[name]
    def __SetEntryInWindow(window : tkinter.Tk, text : str) -> tkinter.Entry:
        entry = tkinter.Entry(window)
        entry.insert(0, text)
        return entry
    def GetEntry(name) -> tkinter.Entry:
        return Util.__entryList[name]

    __frameList = {str : tkinter.Frame}
    def AddFrame(name : str, root : tkinter.Tk, size : Vector2, position : Vector2) -> tkinter.Frame:
        Util.__frameList[name] = Util.__SetFrameInWindow(root, size, position)
        return Util.__frameList[name]
    def __SetFrameInWindow(window : tkinter.Tk, size : Vector2, position : Vector2) -> tkinter.Frame:
        frame = tkinter.Frame(window)
        frame.place(x=position.x, y=position.y, width=size.x, height=size.y)
        return frame
    def GetFrame(name) -> tkinter.Frame:
        return Util.__frameList[name]

    __scrollBarList = {str : tkinter.Scrollbar}
    def AddScrollBar(name : str, root : tkinter.Tk, size : Vector2, position : Vector2, orient : str) -> tkinter.Scrollbar:
        Util.__scrollBarList[name] = Util.__SetScrollBarInWindow(root, size, position, orient)
        return Util.__scrollBarList[name]
    def __SetScrollBarInWindow(window : tkinter.Tk, size : Vector2, position : Vector2, orient : str) -> tkinter.Scrollbar:
        scrollBar = tkinter.Scrollbar(window, orient=orient)
        scrollBar.place(x=position.x, y=position.y, width=size.x, height=size.y)
        return scrollBar
    def GetScrollBar(name) -> tkinter.Scrollbar:
        return Util.__scrollBarList[name]

    __listBoxList = {str : tkinter.Listbox}
    def AddListBox(name : str, root : tkinter.Tk, size : Vector2, position : Vector2, scrollBar : tkinter.Scrollbar) -> tkinter.Listbox:
        Util.__listBoxList[name] = Util.__SetListBoxInWindow(root, size, position, scrollBar)
        return Util.__listBoxList[name]
    def __SetListBoxInWindow(window : tkinter.Tk, size : Vector2, position : Vector2, scrollBar : tkinter.Scrollbar) -> tkinter.Listbox:
        listBox = tkinter.Listbox(window, yscrollcommand=scrollBar.set)
        listBox.place(x=position.x, y=position.y, width=size.x, height=size.y)
        scrollBar.config(command=listBox.yview)
        return listBox
    def GetListBox(name) -> tkinter.Listbox:
        return Util.__listBoxList[name]

    __imgList = {str: tkinter.Image}
    def AddImage(name : str, root : tkinter.Tk, size : Vector2, path : str) -> tkinter.Image :
        Util.__imgList[name] = Util.__SetImageInWindow(root, size, path)
        return Util.__imgList[name]
    def GetImage(name) -> tkinter.Label :
        return Util.__imgList[name]

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

    def __SetImageInWindow(window : tkinter.Tk, size : Vector2, path : str) -> tkinter.Label:
        originImage = Image.open(path)
        resizedImage = originImage.resize((size.x, size.y))
        tkImage = ImageTk.PhotoImage(resizedImage) 
        label = tkinter.Label(window, image=tkImage)
        label.image = tkImage
        label.place(x=0, y=0, width=size.x, height=size.y)
        return label

    def __SetLabelInWindow(window : tkinter.Tk, text : str) :
        label = tkinter.Label(window, text=text)
        return label

    def __SetButtonInWindow(window : tkinter.Tk, text : str, command) -> tkinter.Button:
        button = tkinter.Button(window, text=text, command=command)
        return button