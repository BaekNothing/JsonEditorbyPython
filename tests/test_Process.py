import unittest
import os
import sys

sys.path.append("sources")
from sources import Process


class TestProcess(unittest.TestCase) :
    def test_process_exists(self) :
        self.assertTrue(Process.process_exists("code"))

    def test_getAllProcess(self) :
        self.assertTrue(Process.getAllProcess())
