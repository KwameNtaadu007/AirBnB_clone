#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_initialization(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_place_id(self):
        review = Review()
        review.place_id = "123"
        self.assertEqual(review.place_id, "123")

    # Add more test methods for other attributes as needed

if __name__ == '__main__':
    unittest.main()

