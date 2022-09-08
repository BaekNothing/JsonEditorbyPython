import psutil
import unittest


def process_exists(name : str) -> bool : 
    allProcess = getAllProcess()
    for process in allProcess :
        if process.lower().__contains__(name.lower()) :
            return True
    return False

def getAllProcess() -> list[str] : 
    result : str = []
    for proc in psutil.process_iter() : 
        try :
            result += [proc.name()]
        except psutil.Error :
            print("Error :".  proc.name)
    return result