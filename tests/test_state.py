#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_initialization(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_state_name(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_to_dict(self):
        state = State()
        state.name = "New York"
        state_dict = state.to_dict()
        expected_dict = {
            'id': state.id,
            'created_at': state.created_at.isoformat(),
            'updated_at': state.updated_at.isoformat(),
            'name': "New York",
            '__class__': 'State'
        }
        self.assertDictEqual(state_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

