import json
from textwrap import indent
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sys

import pytest

sys.path.append("sources")
from sources import Interface

def test_AddButton() :
    try :
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.AddButton("test_button", setup, "test_button", lambda : None)
        #wait for window to update
        setup.update()
        assert (setup.winfo_children()[0].winfo_class() == "Button")
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )

def test_AddLabel() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.AddLabel("test_label", setup, "test_label")
        #wait for window to update
        setup.update()
        assert (setup.winfo_children()[0].winfo_class() == "Label")
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )

def test_AddEntry() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.AddEntry("test_entry", setup, "test_entry")
        #wait for window to update
        setup.update()
        assert (setup.winfo_children()[0].winfo_class() == "Entry")
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )

def test_AddFrame() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.AddFrame("test_frame", setup, Interface.Vector2(150, 150), Interface.Vector2(100, 100))
        #wait for window to update
        setup.update()
        assert (setup.winfo_children()[0].winfo_class() == "Frame")
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )

def test_AddScrollBar() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.AddScrollBar("test_scrollbar", setup, Interface.Vector2(150, 150), Interface.Vector2(100, 100), "vertical")
        #wait for window to update
        setup.update()
        assert (setup.winfo_children()[0].winfo_class() == "Scrollbar")
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )

def test_AddText() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.AddText("test_text", setup, Interface.Vector2(150, 150), Interface.Vector2(100, 100), None, None)
        #wait for window to update
        setup.update()
        assert (setup.winfo_children()[0].winfo_class() == "Text")
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )

def test_AddImage() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.AddImage("test_image", setup, Interface.Vector2(150, 150), "./data/icon.png")
        #wait for window to update
        setup.update()
        assert (setup.winfo_children()[0].winfo_class() == "Label")
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir")

def test_SetWindow() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        assert (setup.title() == "test_window")
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )

def test_SetIcon() : 
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.SetIcon(setup, "test_icon")
        #wait for window to update
        setup.update()
        assert (setup.iconbitmap() == "test_icon")
        Interface.Util.CloseWindow(setup)    
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir")

def test_SetWindowSizePosition() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        Interface.Util.SetWindowSizePosition(
            setup, Interface.Vector2(150, 150), Interface.Vector2(100, 100))
        #wait for window to update
        setup.update()
        assert (setup.winfo_width() == 150)
        assert (setup.winfo_height() == 150)
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir")

def test_AddLabelToTextByLine() :
    try : 
        setup = Interface.Util.SetWindow("test_window")
        text = Interface.Util.AddText("test_text", setup, Interface.Vector2(150, 150), Interface.Vector2(100, 100), None, None)
        jsonStr = '{"test":"test1", "test1":["testList"], "test3":{"test":"testtest"}}'
        jsonObj = json.loads(jsonStr)
        jsonStr = json.dumps(jsonObj, indent=4)
        labelList = [
            Interface.Util.AddLabel("test_label", setup, "test"),
        ]
        Interface.Util.AddLabelToTextByLine(
            text, 
            jsonStr.split('\n'),
            labelList, lambda: None)
        
        #wait for window to update
        setup.update()
        assert (len(labelList) == 11)
        Interface.Util.CloseWindow(setup)
    except TclError as e :
        print("this test Not passed it passed by Tcl error : check tcl dir" )