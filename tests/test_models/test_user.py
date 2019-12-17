#!/usr/bin/python3
"""
Unittest for user.py
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    """Unittest for User class"""

    def test_class_attributes(self):
        '''Testin class attributes'''
        obj = User()

        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")
