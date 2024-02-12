#!/usr/bin/env python3
"""
Test the StateModel module for the HBNB project
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewModel(unittest.TestCase):
    """
    Test the TestReviewModel class for the HBNB project
    """
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        """
        Tear down the test
        """
    #   Review.clear()
        del self.review

    def test_review_inherits_from_base_model(self):
        """
        Test that the Review class inherits from BaseModel
        """
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        """Test that the Review class has the correct attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_attributes_default_values(self):

        """Test that the Review class has the correct default values for attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
