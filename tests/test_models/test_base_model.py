#!/usr/bin/python3
"""Unittest for base_model.py
"""

import unittest
from io import StringIO
from unittest.mock import patch
import datetime
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """Unittest for BaseModel"""

    def test_init_with_kwargs(self):
        """
        Creating an instance passing
        keyworded arguments
        """
        dictionary = {"Name": 'bob', "Num": 1}
        instance = BaseModel(**dictionary)

        self.assertEqual(instance.Name, 'bob')
        self.assertEqual(instance.Num, 1)

    def test_init_with_args(self):
        """
        Creating an instance passing
        non keyworded arguments
        """
        instance = BaseModel('Hello')

    def test_init_no_args(self):
        """Passing no arguments to BaseModel"""
        instance = BaseModel()

    def test_str(self):
        """Testing str method"""
        instance = BaseModel()

        self.maxDiff = None

        expected = "[BaseModel] ({}) {}\n".format(
            instance.id, instance.__dict__)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(instance)
            self.assertEqual(fake_out.getvalue(), expected)

    def testing_save(self):
        """Testing save method"""
        instance = BaseModel()

        before = instance.updated_at

        instance.save()

        now = instance.updated_at

        self.assertNotEqual(before, now)

    def testing_to_dict(self):
        """Testing to_dict method"""
        instance = BaseModel()

        dictionary = instance.to_dict()

        self.assertIsInstance(dictionary, dict)

    def test_attributes(self):
        """Testing attributes"""
        instance = BaseModel()
        self.assertIs(type(instance.id), str)
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))
        self.assertFalse(instance.updated_at == datetime.now())


if __name__ == '__main__':
    unittest.main()
