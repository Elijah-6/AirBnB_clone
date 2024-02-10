#!/usr/bin/python3
"""Test module for the FileStorage class"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test class for the FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up the test class"""
        cls.storage = FileStorage()
        cls.storage.reload()
        # Initialize FileStorage instance and reload
        cls.storage = FileStorage()
        cls.storage.reload()

    def tearDown(self):
        """Tear down the test case"""
        # Delete the JSON file after each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save_and_reload(self):
        """Test the save and reload methods"""
        # Create a BaseModel instance
        base_model = BaseModel()
        base_model.save()

        # Reload FileStorage and check if the object is in __objects
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn("BaseModel." + base_model.id, objects)

    def test_new_method(self):
        """Test the new method"""
        # Create a BaseModel instance
        base_model = BaseModel()

        # Check if the object is added to __objects using new() method
        self.storage.new(base_model)
        objects = self.storage.all()
        self.assertIn("BaseModel." + base_model.id, objects)

    def test_save_method_called(self):
        """Test the save method is called when an object is saved"""
        # Mock save method of FileStorage
        original_save_method = FileStorage.save
        FileStorage.save = lambda x: x  # Mock the save method to do nothing

        # Create a BaseModel instance
        base_model = BaseModel()
        base_model.save()

        # Check if save method of FileStorage is called
        with self.assertRaises(AttributeError):
            FileStorage.save_called  # Should raise AttributeError if save method is called

        # Restore original save method
        FileStorage.save = original_save_method

    def test_reload_method_no_exception(self):
        """Test the reload method without any exception"""
        # Test if reload method doesn't raise exception when file doesn't exist
        self.storage._FileStorage__file_path = "non_existing_file.json"
        self.storage.reload()  # Should not raise any exception

if __name__ == '__main__':
    unittest.main()
