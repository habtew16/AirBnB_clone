#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8


class TestFileStorage(unittest.TestCase):
    """
    testing file storage
    """

    @classmethod
    def setUpClass(self):
        self.storage = FileStorage()

    @classmethod
    def teardown(self):
        pass

    def teardown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_filestorage(self):
        """
        tests for pep8
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all_filestorage(self):
        """
        tests for all
        """
        new = FileStorage()
        instances_dic = new.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, new._FileStorage__objects)

    def test_new_filestorage(self):
        """
        tests for new
        """
        pass

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()

        try:
            os.remove(path)
        except Exception:
            pass

        self.storage.save()

        with open(path, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(path)
        except Exception:
            pass

        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
