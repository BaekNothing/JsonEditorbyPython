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

def test_GetJsonString(setup) :
    assert JsonParser.GetJsonString() == ""

def test_SetJsonData(setup) :
    assert JsonParser.SetJsonData({"test" : "test"}) == {"test" : "test"}

def test_CheckJsonAble(setup) :
    assert JsonParser.CheckJsonAble('{"test" : "test"}') == True
    assert JsonParser.CheckJsonAble("test") == False

def test_MakeJsonToString(setup) :
    assert JsonParser.MakeJsonToString({"test" : "test"}) == "{\n    \"test\": \"test\"\n}"

def test_SetJsonData(setup) :
    assert JsonParser.SetJsonData({"test" : "test"}) == {"test" : "test"}

def test_GetJsonValue(setup) :
    assert JsonParser.GetJsonValue("test") == "test"
    assert JsonParser.GetJsonValue("dict") == {"test" : "test"}
    assert JsonParser.GetJsonValue("list") == ["test", "test"]

def test_GetJsonkeys(setup) :
    assert JsonParser.GetJsonkeys({"test" : "test"}) == ["test"]

