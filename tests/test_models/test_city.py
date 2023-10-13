#!/usr/bin/python3
"""This is the unittest module for the City Class."""

import unittest
from models.city import City
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import sys
sys.path.append("..")

class TestCity(unittest.TestCase):

    """These are test Cases for the City class."""

    def setUp(self):
        """This sets up test methods."""
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
        """This tests the instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """This tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()

