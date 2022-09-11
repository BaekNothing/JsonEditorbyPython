import os 
import tkinter
import tkinter.filedialog

from PIL import Image

def ReadFile(filePath : str) -> str :
    with open(filePath, "r", encoding='utf-8') as file:
        return file.read()

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