#!/usr/bin/python3

""" The file_storage.py module to define the class FileStorage """


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class FileStorage:
    
    """ Class FileStorage class functions to serialize instances to a JSON file
        and also to deserialize the JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ funct to return the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """funct to set in the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """funct to serialize __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ funct to deserialize the JSON file to __objects """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
