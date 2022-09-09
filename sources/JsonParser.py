import psutil
import unittest
import json
import JsonParser
import File

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
    __jsonData = JsonParser.ValueToJson(File.ReadFile(path))
    return __jsonData

def MakeJsonToString(inputJson : json) -> str:
    __jsonString = json.dumps(inputJson, indent=4)
    return __jsonString

def ValueToJson(value : any) -> json:
    value = str(value).replace("\'", "\"")
    return json.loads(value)

def GetJsonkeys(inputJson : json) -> list:
    return list(inputJson.keys())

def GetJsonValue(key : str) -> json:
    return __jsonData[key]
