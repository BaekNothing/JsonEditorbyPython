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
    __btnList = {}
    def AddButton(name : str, root : tkinter.Tk, text : str, command) -> None :
        Util.__btnList[name] = Util.__SetButtonInWindow(root, text, command)
    def GetButton(name) -> tkinter.Button :
        return Util.__btnList[name]

    __lblList = {}
    def AddLabel(name : str, root : tkinter.Tk, text : str) -> None :
        Util.__lblList[name] = Util.__SetLabelInWindow(root, text)
    def GetLabel(name) -> tkinter.Label :
        return Util.__lblList[name]

    __imgList = {}
    def AddImage(name : str, root : tkinter.Tk, size : Vector2, path : str) -> None :
        Util.__imgList[name] = Util.__SetImageInWindow(root, size, path)
    def GetImage(name) -> tkinter.Label :
        return Util.__imgList[name]

    def ShowMessage(msgtitle : str, msgmessage : str):
        tkinter.messagebox.showinfo(title=msgtitle, message=msgmessage)

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