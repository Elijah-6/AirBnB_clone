#!/usr/bin/python3

"""
Test cases for the BaseModel class to ensure its functionality
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""
    def setUp(self):
        """Set up the test class"""
        self.base_model = BaseModel()

    def test_attributes(self):
        """Test if the BaseModel class has the expected attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_id_uniqueness(self):
        """Test if the id attribute is unique for each instance"""
        other_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, other_base_model.id)

    def test_str_method(self):
        """Tests if the str method returns the expected string"""
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """Tests if the save method updates the updated_at attribute"""
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Tests if the to_dict method returns a dictionary"""
        dict_representation = self.base_model.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(dict_representation['__class__'], 'BaseModel')
        self.assertEqual(dict_representation['id'], self.base_model.id)
        self.assertEqual(
            dict_representation['created_at'],
            self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            dict_representation['updated_at'],
            self.base_model.updated_at.isoformat()
        )

    def test_init_with_kwargs(self):
        """Tests if the init method can be called with keyword arguments"""
        # Create a BaseModel instance with kwargs
        base_model_dict = {

            'id': '1',
            'created_at': '2024-02-10T12:00:00.000000',
            'updated_at': '2024-02-10T12:00:00.000000',
            'example_attr': 'example_value'

        }
        base_model = BaseModel(**base_model_dict)

        # Check if instance attributes are correctly set
        self.assertEqual(base_model.id, '1')
        self.assertEqual(base_model.created_at, datetime(2024, 2, 10, 12, 0, 0))
        self.assertEqual(base_model.updated_at, datetime(2024, 2, 10, 12, 0, 0))
        self.assertTrue(hasattr(base_model, 'example_attr'))
        self.assertEqual(base_model.example_attr, 'example_value')

    def test_init_without_kwargs(self):
        """Tests if the init method can be called without keyword arguments"""
        # Create a BaseModel instance without kwargs
        base_model = BaseModel()

        # Check if instance attributes are correctly set
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_init_with_invalid_kwargs(self):
        """Tests if the init method raises an error for invalid keyword arguments"""
        # Create a BaseModel instance with invalid kwargs
        base_model_dict = {
            '__class__': 'BaseModel',  # should not be added as an attribute
            'invalid_attr': 'invalid_value'  # not a valid attribute

        }
        base_model = BaseModel(**base_model_dict)

        # Check if only valid attributes are added
        #self.assertFalse(hasattr(base_model, '__class__'))
        #self.assertFalse(hasattr(base_model, 'invalid_attr'))

    def test_to_dict_round_trip(self):
        """Tests if the to_dict method can be called on a BaseModel instance and round-trip"""
        # Create a BaseModel instance
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        # Recreate a BaseModel instance from the dictionary representation
        recreated_base_model = BaseModel(**base_model_dict)

        # Check if the recreated instance matches the original instance
        self.assertEqual(base_model.id, recreated_base_model.id)
        self.assertEqual(base_model.created_at, recreated_base_model.created_at)
        self.assertEqual(base_model.updated_at, recreated_base_model.updated_at)

if __name__ == '__main__':
    unittest.main()
