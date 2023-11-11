#!/usr/bin/python3
"""Tests the basemodels"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """tests for basemodel"""
    @classmethod
    def setUp(self):
        """sets up"""
        self.testBase = BaseModel()
        self.testBase.x = "x"
        self.testBase.y = 100

    @classmethod
    def tearDown(self):
        """
        tears down
        """
        del self.testBase
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_basemodel(self):
        """
        tests pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_check_functions(self):
        """function to check if class has
        doc file"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attribute_basemodel(self):
        """function to check if attributes exist
        in basemodel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """check the existance of init"""
        self.assertTrue(isinstance(self.testBase, BaseModel))

    def test_save(self):
        """check save"""
        self.testBase.save()
        self.assertNotEqual(self.testBase.created_at, self.testBase.updated_at)

    def test_to_dict(self):
        """checkes to dict function of basemodel"""
        obj = self.testBase.to_dict()
        self.assertEqual(self.testBase.__class__.__name__, 'BaseModel')
        self.assertIsInstance(obj['created_at'], str)
        self.assertIsInstance(obj['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
