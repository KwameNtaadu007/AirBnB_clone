#!/usr/bin/python3
""" Unit test City """

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_initialization(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_state_id(self):
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_city_name(self):
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_city_to_dict(self):
        city = City()
        city.state_id = "NY"
        city.name = "New York"
        city_dict = city.to_dict()
        expected_dict = {
            'id': city.id,
            'created_at': city.created_at.isoformat(),
            'updated_at': city.updated_at.isoformat(),
            'state_id': "NY",
            'name': "New York",
            '__class__': 'City'
        }
        self.assertDictEqual(city_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

