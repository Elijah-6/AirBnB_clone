#!/usr/bin/python3
"""Test the UserModel module for the HBNB project"""
import unittest
from models.user import User
#from models.engine.file_storage import FileStorage
from console import HBNBCommand
import os


class TestUserModel(unittest.TestCase):
    """Test the UserModel class for the HBNB project"""
    def setUp(self):
        self.user = User()

    def tearDown(self):
        """Tear down the test"""
        # User.clear()
        del self.user

    # def test_user_inherits_from_base_model(self):
    #     self.assertIsInstance(self.user, User)
    #     self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """Test if User attributes are initialized correctly"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_attributes_default_values(self):
        """Test if User attributes have default values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_attributes_type(self):
        """Test if User attributes have the correct type"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_user_attributes_setter(self):
        """Test if User attributes can be set"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_user_attributes_to_dict(self):
        """Test if User attributes can be converted to a dictionary"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")

if __name__ == '__main__':
    unittest.main()
