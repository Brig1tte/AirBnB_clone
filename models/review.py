#!/usr/bin/env python3

""" This Module is a function to implement the Class Review """

from models.base_model import BaseModel

class Review(BaseModel):
    
    """ The Class Review to be inherited from the BaseModel """

    place_id = ""
    user_id = ""
    text = ""
