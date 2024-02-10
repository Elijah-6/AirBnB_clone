#!/usr/bin/env bash
"""
Test the StateModel module for the HBNB project
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenityModel(unittest.TestCase):
    """
    Test the AmenityModel class for the HBNB project
    """    
    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        """
        Tear down the test class
        """
        del self.amenity

    def test_amenity_inherits_from_base_model(self):
        """
        Test if Amenity inherits from BaseModel in the HBNB project
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """
        Test if Amenity attributes are initialized correctly
        """
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_attributes_default_values(self):
        """
        Test if Amenity attributes have default values
        """
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
