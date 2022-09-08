import unittest
import os
import sys

from PIL import Image
import pytest
import shutil

sys.path.append("sources")
from sources import File

#setup

@pytest.fixture
def setup() :
    try :
        shutil.rmtree("test")
    except :
        pass
    os.mkdir("test")
    File.SaveFile(os.getcwd() + "\\test\\test.txt", "test")
    yield
    shutil.rmtree("test")

def test_CheckDirExist(setup) :
    assert File.CheckDirExist(os.getcwd() + "\\test") == True

def test_CheckFileExist(setup) :
    assert File.CheckFileExist(os.getcwd() + "\\test\\test.txt") == True

def test_SaveFile(setup) :
    assert File.SaveFile(os.getcwd() + "\\test\\test.txt", "test") == True

def test_ReadFile(setup) :
    assert File.ReadFile(os.getcwd() + "\\test\\test.txt") == "test"

def test_SaveCapturedImage(setup) :
    assert File.SaveCapturedImage(os.getcwd() + "\\test.png", Image.new("RGB", (100, 100))) == True

def test_GetFilesInDir(setup) :
    assert File.GetFilesInDir(os.getcwd()) != []

