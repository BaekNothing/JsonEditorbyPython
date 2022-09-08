import os
import sys

import pytest

sys.path.append("sources")
from sources import JsonParser

@pytest.fixture
def setup() :
    JsonParser.SetJsonData({"test" : "test", "dict" : {"test" : "test"}, "list" : ["test", "test"]})
    yield
    JsonParser.SetJsonData({})

def test_SetJsonData(setup) :
    assert JsonParser.SetJsonData({"test" : "test"}) == {"test" : "test"}

def test_GetJsonValue(setup) :
    assert JsonParser.GetJsonValue("test") == "test"
    assert JsonParser.GetJsonValue("dict") == {"test" : "test"}
    assert JsonParser.GetJsonValue("list") == ["test", "test"]

def test_GetJsonkeys(setup) :
    assert JsonParser.GetJsonkeys({"test" : "test"}) == ["test"]

def test_StringToJson(setup) :
    assert JsonParser.StringToJson("{\"test\" : \"test\"}") == {"test" : "test"}

def test_JsonToString(setup) :
    assert JsonParser.JsonToString({"test" : "test"}) == "{\"test\": \"test\"}"

def test_SaveJsonToFile(setup) :
    JsonParser.SaveJsonToFile("test.json")

def test_SetJsonDataFromFile(setup) :
    assert JsonParser.SetJsonDataFromFile("./tests/test.json") == {"test" : "test"}
