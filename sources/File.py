import os 
import tkinter

from PIL import Image

def CheckDirExist(dir : str) -> bool :
    return os.path.isdir(dir)

def CheckFileExist(file : str) -> bool :
    return os.path.isfile(file)

def SaveFile(filePath : str, content : str) -> bool :
    try:
        with open(filePath, "w") as file:
            file.write(content)
        return True
    except:
        return False

def ReadFile(filePath : str) -> str :
    try:
        with open(filePath, "r") as file:
            return file.read()
    except:
        return ""

def SaveCapturedImage(filePath : str, image : Image) -> bool :
    try:
        image.save(filePath)
        return True
    except:
        return False

def GetFilesInDir(dir : str) -> list :
    try:
        return os.listdir(dir)
    except:
        return []

def ShowFileDialog() -> os.__file__:
        return tkinter.filedialog.askopenfilename(
            title="Open File",
            initialdir=os.getcwd(),
            filetypes=[("All Files", "*.*"), ("Python Files", "*.py")]
        )

def ShowSaveFileDialog(file : os.__file__) -> os.__file__ : 
    return tkinter.filedialog.asksaveasfile(
        title="Save File",
        initialdir=os.getcwd(),
        initialfile=file,
        filetypes=[("All Files", "*.*"), ("Python Files", "*.py")]
    )