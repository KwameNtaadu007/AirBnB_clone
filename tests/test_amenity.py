#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_initialization(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_amenity_name(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_amenity_to_dict(self):
        amenity = Amenity()
        amenity.name = "Gym"
        amenity_dict = amenity.to_dict()
        expected_dict = {
            'id': amenity.id,
            'created_at': amenity.created_at.isoformat(),
            'updated_at': amenity.updated_at.isoformat(),
            'name': "Gym",
            '__class__': 'Amenity'
        }
        self.assertDictEqual(amenity_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

