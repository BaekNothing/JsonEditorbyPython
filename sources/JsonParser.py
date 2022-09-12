import json
import sys

sys.path.append("./")
from . import File

__jsonData = {}
__jsonString = ""

def GetJsonString() -> str:
    return __jsonString

def SetJsonData(json) -> json:
    global __jsonData
    __jsonData = json
    return __jsonData

def SetJsonDataFromFile(path : str) -> json:
    global __jsonData
    __jsonData = ValueToJson(File.ReadFile(path))
    return __jsonData

def CheckJsonAble(input : str) -> bool:
    try:
        json.loads(str(input))
    except ValueError:
        return False
    return True

def MakeJsonToString(inputJson : json) -> str:
    __jsonString = json.dumps(inputJson, indent=4)
    return __jsonString

def ValueToJson(value : any) -> json:
    return json.loads(value)

def GetJsonkeys(inputJson : json) -> list:
    return list(inputJson.keys())

def GetJsonValue(key : str) -> json:
    return __jsonData[key]
