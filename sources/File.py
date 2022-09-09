import os 
import tkinter
import tkinter.filedialog

from PIL import Image

def CheckDirExist(dir : str) -> bool :
    return os.path.isdir(dir)

def CheckFileExist(file : str) -> bool :
    return os.path.isfile(file)

def SaveFile(filePath : str, content : str) :
    with open(filePath, "a", encoding='utf-8') as file:
        file.write(content)

def ReadFile(filePath : str) -> str :
    with open(filePath, "r", encoding='utf-8') as file:
        return file.read()

def SaveCapturedImage(filePath : str, image : Image) :
    image.save(filePath)

def GetFilesInDir(dir : str) -> list :
    return os.listdir(dir)

def ShowFileDialog() -> os.__file__:
    try :
        return tkinter.filedialog.askopenfilename(
            title="Open File",
            initialdir=os.getcwd(),
            filetypes=[("All Files", "*.*"), ("Python Files", "*.py")]
        )
    except FileNotFoundError :
        return None

def ShowSaveFileDialog() -> os.__file__ : 
    return tkinter.filedialog.asksaveasfile(
        title="Save File",
        initialdir=os.getcwd(),
        filetypes=[("All Files", "*.*"), ("Python Files", "*.py")]
    )