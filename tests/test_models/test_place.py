#!/usr/bin/python3
import unittest
import os
import pep8
from models.place import Place
from datetime import datetime
import models


class TestPlace(unittest.TestCase):

    def test_pep8_place(self):
        """
        Test that models/place.py conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_place_instance(self):
        """
        Test the instantiation of the Place class.
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_city_id_type(self):
        """
        Test the type of the city_id attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.city_id, str)

    def test_place_user_id_type(self):
        """
        Test the type of the user_id attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.user_id, str)

    def test_place_name_type(self):
        """
        Test the type of the name attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.name, str)

    def test_place_description_type(self):
        """
        Test the type of the description attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.description, str)

    def test_place_number_rooms_type(self):
        """
        Test the type of the number_rooms attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.number_rooms, int)

    def test_place_number_bathrooms_type(self):
        """
        Test the type of the number_bathrooms attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.number_bathrooms, int)

    def test_place_max_guest_type(self):
        """
        Test the type of the max_guest attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.max_guest, int)

    def test_place_price_by_night_type(self):
        """
        Test the type of the price_by_night attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.price_by_night, int)

    def test_place_latitude_type(self):
        """
        Test the type of the latitude attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.latitude, float)

    def test_place_longitude_type(self):
        """
        Test the type of the longitude attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.longitude, float)

    def test_place_amenity_ids_type(self):
        """
        Test the type of the amenity_ids attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.amenity_ids, str)

    def test_place_created_at_type(self):
        """
        Test the type of the created_at attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.created_at, datetime)

    def test_place_updated_at_type(self):
        """
        Test the type of the updated_at attribute in Place.
        """
        place = Place()
        self.assertIsInstance(place.updated_at, datetime)

    def test_place_save(self):
        """
        Test the save method in Place.
        """
        place = Place()
        prev_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(prev_updated_at, place.updated_at)

    def test_place_to_dict(self):
        """
        Test the to_dict method in Place.
        """
        place = Place()
        obj_dict = place.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Place')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_place_str(self):
        """
        Test the __str__ method in Place.
        """
        place = Place()
        expected_str = "[Place] ({}) {}".format(
            place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

    def test_place_repr(self):
        """
        Test the __repr__ method in Place.
        """
        place = Place()
        expected_repr = str(place)
        self.assertEqual(repr(place), expected_repr)


if __name__ == '__main__':
    unittest.main()
