#!/usr/bin/python3
"""Unittest for file_storage.py
"""

import unittest
import os
from io import StringIO
from unittest.mock import patch

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    """Unittest for FileStorage"""

    def test_new(self):
        '''Testing new method'''
        storage = FileStorage()
        obj_1 = BaseModel()
        storage.new(obj_1)

        objects = storage.all()

        self.assertEqual(objects['BaseModel' + "." + obj_1.id], obj_1)

    def test_all(self):
        '''Testing all method'''
        storage = FileStorage()
        obj_1 = BaseModel()
        storage.new(obj_1)

        self.assertIs(type(storage.all()), dict)
        self.assertTrue(len(storage.all()) != 0)

    def test_save(self):
        '''Testing save method'''
        storage = FileStorage()
        obj_1 = BaseModel()
        storage.new(obj_1)
        storage.save()

        self.assertTrue(os.stat('file.json').st_size != 0)

    def test_reload(self):
        '''Testing reload method'''
        storage = FileStorage()
        storage.reload()

        self.assertTrue(os.stat('file.json').st_size != 0)


if __name__ == '__main__':
    unittest.main()
