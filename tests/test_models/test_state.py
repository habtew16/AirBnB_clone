#!/usr/bin/python3
import unittest
import os
import pep8
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):

    def test_pep8_state(self):
        """
        Test that models/state.py conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_state_instance(self):
        """
        Test the instantiation of the State class.
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name_type(self):
        """
        Test the type of the name attribute in State.
        """
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_created_at_type(self):
        """
        Test the type of the created_at attribute in State.
        """
        state = State()
        self.assertIsInstance(state.created_at, datetime)

    def test_state_updated_at_type(self):
        """
        Test the type of the updated_at attribute in State.
        """
        state = State()
        self.assertIsInstance(state.updated_at, datetime)

    def test_state_save(self):
        """
        Test the save method in State.
        """
        state = State()
        prev_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(prev_updated_at, state.updated_at)

    def test_state_to_dict(self):
        """
        Test the to_dict method in State.
        """
        state = State()
        obj_dict = state.to_dict()
        self.assertEqual(obj_dict['__class__'], 'State')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_state_str(self):
        """
        Test the __str__ method in State.
        """
        state = State()
        expected_str = "[State] ({}) {}".format(
            state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

    def test_state_repr(self):
        """
        Test the __repr__ method in State.
        """
        state = State()
        expected_repr = str(state)
        self.assertEqual(repr(state), expected_repr)


if __name__ == '__main__':
    unittest.main()
