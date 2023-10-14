#!/usr/bin/env python3

""" This Module implements the Class from BaseModel """

from models.base_model import BaseModel

class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
