#!/usr/bin/python3
"""This is the unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import sys
sys.path.append("..")



class TestAmenity(unittest.TestCase):

    """This is the test Cases for the Amenity class."""

    def setUp(self):
        """This sets up test methods."""
        pass

    def tearDown(self):
        """This tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """This resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """This tests the instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """This tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()

