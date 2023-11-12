#!/usr/bin/python3
import unittest
import os
import pep8
from datetime import datetime
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):

    def test_pep8_base_model(self):
        """
        Test that models/base_model.py conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_base_model_instance(self):
        """
        Test the instantiation of the BaseModel class.
        """
        test_base = BaseModel()
        self.assertIsInstance(test_base, BaseModel)

    def test_base_model_id_type(self):
        """
        Test the type of the id attribute in BaseModel.
        """
        test_base = BaseModel()
        self.assertIsInstance(test_base.id, str)

    def test_base_model_created_at_type(self):
        """
        Test the type of the created_at attribute in BaseModel.
        """
        test_base = BaseModel()
        self.assertIsInstance(test_base.created_at, datetime)

    def test_base_model_updated_at_type(self):
        """
        Test the type of the updated_at attribute in BaseModel.
        """
        test_base = BaseModel()
        self.assertIsInstance(test_base.updated_at, datetime)

    def test_base_model_save(self):
        """
        Test the save method in BaseModel.
        """
        test_base = BaseModel()
        prev_updated_at = test_base.updated_at
        test_base.save()
        self.assertNotEqual(prev_updated_at, test_base.updated_at)

    def test_base_model_to_dict(self):
        """
        Test the to_dict method in BaseModel.
        """
        test_base = BaseModel()
        obj_dict = test_base.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_base_model_str(self):
        """
        Test the __str__ method in BaseModel.
        """
        test_base = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            test_base.id, test_base.__dict__)
        self.assertEqual(str(test_base), expected_str)

    def test_base_model_repr(self):
        """
        Test the __repr__ method in BaseModel.
        """
        test_base = BaseModel()
        expected_repr = str(test_base)
        self.assertEqual(repr(test_base), expected_repr)


if __name__ == '__main__':
    unittest.main()
