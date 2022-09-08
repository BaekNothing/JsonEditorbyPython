import psutil
import unittest
import json
import JsonParser
import File

__jsonData = {}

def SetJsonData(json) -> dict:
    global __jsonData
    __jsonData = json
    return __jsonData

def SetJsonDataFromFile(path : str) -> json:
    global __jsonData
    __jsonData = JsonParser.ValueToJson(File.ReadFile(path))
    return __jsonData

def ValueToJson(value : any) -> json:
    return json.loads(str(value))

def GetJsonkeys(json : json) -> list:
    return list(json.keys())

def GetJsonValue(key : str) -> json:
    return __jsonData[key]
