import unittest
import sys

import pytest

sys.path.append("sources")
from sources import Interface

@pytest.fixture
def setup() :
    window = Interface.Util.SetWindow("test")
    yield window
    Interface.Util.CloseWindow(window)

def test_SetWindow(setup) :
    assert setup != None

def test_SetWindowSizePosition(setup) :
    Interface.Util.SetWindowSizePosition(
        setup, Interface.Vector2(150, 150), Interface.Vector2(100, 100))
    #wait for window to update
    setup.update()
    assert (setup.winfo_width() == 150)
    assert (setup.winfo_height() == 150)
    
def test_AddLabel(setup) :
    Interface.Util.AddLabel("test", setup, "test")
    assert Interface.Util.GetLabel("test") != None

def test_AddButton(setup) :
    Interface.Util.AddButton("test", setup, "test", None)
    assert Interface.Util.GetButton("test") != None

def test_AddImage(setup) :
    Interface.Util.AddImage("test", setup, Interface.Vector2(100, 100), "data/image/icon.png")
    assert Interface.Util.GetImage("test") != None