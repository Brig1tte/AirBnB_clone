#!/usr/bin/python3

""" The Amenity class of the models.amenity module test cases """

from models.amenity import Amenity
import unittest
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    def test_amenity_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def setUp(self):
        self.amenity = Amenity()

    def test_class_attr(self):
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.amenity, "name"))

