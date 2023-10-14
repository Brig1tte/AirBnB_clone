#!/usr/bin/python3

"""A module to handle all the test cases in relation to the BaseModel Class"""

from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ function to define test cases for the BaseModel class """

    def setUp(self):
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_uuid(self):
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertIsInstance(self.bm1.id, str)
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_instance_type(self):
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertIsInstance(str(self.bm1), str)
        self.assertEqual(str(self.bm2),
                        "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_to_dict(self):
        self.assertIsInstance(self.bm2.to_dict(), dict)

    def test_type_created_at(self):
        self.assertIs(self.bm1.created_at, datetime)

    def test_type_updated_at(self):
        self.assertIs(self.bm1.updated_at, datetime)
