#!/usr/bin/python3
"""This is the unittest module for the Place Class."""

import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import sys
sys.path.append("..")

class TestPlace(unittest.TestCase):

    """This test Cases for the Place class."""

    def setUp(self):
        """This sets up the test methods."""
        pass

    def tearDown(self):
        """This tears down the test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """This resets the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """This tests the instantiation of Place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """This tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()

