#!/usr/bin/python3
import unittest
import os
import pep8
from models.city import City
from datetime import datetime
import models


class TestCity(unittest.TestCase):

    def test_pep8_city(self):
        """
        Test that models/city.py conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_city_instance(self):
        """
        Test the instantiation of the City class.
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_city_state_id_type(self):
        """
        Test the type of the state_id attribute in City.
        """
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_city_name_type(self):
        """
        Test the type of the name attribute in City.
        """
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_created_at_type(self):
        """
        Test the type of the created_at attribute in City.
        """
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_city_updated_at_type(self):
        """
        Test the type of the updated_at attribute in City.
        """
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_save(self):
        """
        Test the save method in City.
        """
        city = City()
        prev_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(prev_updated_at, city.updated_at)

    def test_city_to_dict(self):
        """
        Test the to_dict method in City.
        """
        city = City()
        obj_dict = city.to_dict()
        self.assertEqual(obj_dict['__class__'], 'City')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_city_str(self):
        """
        Test the __str__ method in City.
        """
        city = City()
        expected_str = "[City] ({}) {}".format(
            city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)

    def test_city_repr(self):
        """
        Test the __repr__ method in City.
        """
        city = City()
        expected_repr = str(city)
        self.assertEqual(repr(city), expected_repr)


if __name__ == '__main__':
    unittest.main()
