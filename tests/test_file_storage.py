#!/usr/bin/python3
"""
This test for storage
"""

import unittest
from time import sleep
import sys
sys.path.append("..")
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """This test the FileStorage Class"""
    def test_instances(self):
        """chequeamos instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """This test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()

