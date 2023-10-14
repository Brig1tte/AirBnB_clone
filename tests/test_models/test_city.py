#!/usr/bin/python3

""" the Class City of the module models.city """

import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):

    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def setUp(self):
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)
            self.assertFalse(bool(getattr(self.city, attr)))
