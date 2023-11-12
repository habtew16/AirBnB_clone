#!/usr/bin/python3
import unittest
import os
import pep8
from models.review import Review
from datetime import datetime
import models


class TestReview(unittest.TestCase):

    def test_pep8_review(self):
        """
        Test that models/review.py conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_review_instance(self):
        """
        Test the instantiation of the Review class.
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_place_id_type(self):
        """
        Test the type of the place_id attribute in Review.
        """
        review = Review()
        self.assertIsInstance(review.place_id, str)

    def test_review_user_id_type(self):
        """
        Test the type of the user_id attribute in Review.
        """
        review = Review()
        self.assertIsInstance(review.user_id, str)

    def test_review_text_type(self):
        """
        Test the type of the text attribute in Review.
        """
        review = Review()
        self.assertIsInstance(review.text, str)

    def test_review_created_at_type(self):
        """
        Test the type of the created_at attribute in Review.
        """
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_review_updated_at_type(self):
        """
        Test the type of the updated_at attribute in Review.
        """
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)

    def test_review_save(self):
        """
        Test the save method in Review.
        """
        review = Review()
        prev_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(prev_updated_at, review.updated_at)

    def test_review_to_dict(self):
        """
        Test the to_dict method in Review.
        """
        review = Review()
        obj_dict = review.to_dict()
        self.assertEqual(obj_dict['__class__'], 'Review')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_review_str(self):
        """
        Test the __str__ method in Review.
        """
        review = Review()
        expected_str = "[Review] ({}) {}".format(
            review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)

    def test_review_repr(self):
        """
        Test the __repr__ method in Review.
        """
        review = Review()
        expected_repr = str(review)
        self.assertEqual(repr(review), expected_repr)


if __name__ == '__main__':
    unittest.main()
