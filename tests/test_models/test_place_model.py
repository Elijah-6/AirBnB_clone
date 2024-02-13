#!/usr/bin/env python3
"""
Test the test_place_model module for the HBNB project
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceModel(unittest.TestCase):
    """
    Test the PlaceModel class for the HBNB project
    """
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        """
        Tear down the test class
        """
        del self.place

    def test_place_inherits_from_base_model(self):
        """
        Test if Place inherits from BaseModel in the HBNB project
        """
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes(self):
        """
        Test if Place attributes are initialized correctly
        """
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_place_attributes_default_values(self):
        """
        Test if Place attributes have default values
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
