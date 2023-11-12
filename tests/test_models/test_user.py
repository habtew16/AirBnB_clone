#!/usr/bin/python3
"""test class to test user"""
import unittest
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_pep8_user(self):
        """
        Test that models/user.py conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_user_attributes(self):
        """
        Test the attributes of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_inheritance(self):
        """
        Test that User class inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes_default_values(self):
        """
        Test that User attributes have default values.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
