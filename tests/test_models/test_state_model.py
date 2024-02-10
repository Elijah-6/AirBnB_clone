#!/usr/bin/env bash
"""Test the StateModel module for the HBNB project"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateModel(unittest.TestCase):
    """Test the StateModel class for the HBNB project"""
    def setUp(self):
        """Set up the test class"""
        self.state = State()

    def tearDown(self):
        """Tear down the test class"""
        self.state = None
        del self.state

    def test_state_inherits_from_base_model(self):
        """Test if State inherits from BaseModel in the HBNB project"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        """Test if State attributes are initialized correctly"""
        self.assertTrue(hasattr(self.state, 'name'))

    # def test_state_attributes_default_values(self):
    #     """Test if State attributes have default values"""
    #     self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
