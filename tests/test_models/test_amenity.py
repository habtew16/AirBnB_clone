#!/usr/bin/python3
import unittest
import os
import pep8
from models.amenity import Amenity
from datetime import datetime
import models


class TestAmenity(unittest.TestCase):

    def test_pep8_amenity(self):
        """
        Test that models/amenity.py conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_amenity_instance(self):
        """
        Test the instantiation of the Amenity class.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_name_type(self):
        """
        Test the type of the name attribute in Amenity.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_created_at_type(self):
        """
        Test the type of the created_at attribute in Amenity.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_amenity_updated_at_type(self):
        """
        Test the type of the updated_at attribute in Amenity.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_amenity_save(self):
        """
        Test the save method in Amenity.
        """
        amenity = Amenity()
        prev_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(prev_updated_at, amenity.updated_at)

    def test_amenity_to_dict(self):
        """
        Test the to_dict method in Amenity.
        """
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Amenity')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_amenity_str(self):
        """
        Test the __str__ method in Amenity.
        """
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(
            amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_amenity_repr(self):
        """
        Test the __repr__ method in Amenity.
        """
        amenity = Amenity()
        expected_repr = str(amenity)
        self.assertEqual(repr(amenity), expected_repr)


if __name__ == '__main__':
    unittest.main()
