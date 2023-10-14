#!/usr/bin/env python3

""" The Class Review module implementation """

from models.base_model import BaseModel

class Review(BaseModel):
    """ the class review inherits from the baseModel """

    place_id = ""
    user_id = ""
    text = ""
