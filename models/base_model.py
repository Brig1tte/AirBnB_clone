#!/usr/bin/env python3

""" Common attr's for other classes inherited from the BaseModel class """

from models import storage
from datetime import datetime, time, date
import uuid

class BaseModel:
    """This BaseModel class to define attr's id, created_at,
        updated_at and methods """

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dict
