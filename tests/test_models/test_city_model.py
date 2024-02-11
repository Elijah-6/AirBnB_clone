#!/usr/bin/env bash
"""
Test the test_city_model module for the HBNB project
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCityModel(unittest.TestCase):
    """
    Test the CityModel class for the HBNB project
    """
    def setUp(self):
        """
        Set up the test class
        """
        self.city = City()

    def tearDown(self):
        """
        Tear down the test class
        """
        del self.city

    def test_city_inherits_from_base_model(self):
        """
        Test if City inherits from BaseModel in the HBNB project
        """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        """
        Test if City attributes are initialized correctly
        """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_attributes_default_values(self):
        """
        Test if City attributes have default values
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
