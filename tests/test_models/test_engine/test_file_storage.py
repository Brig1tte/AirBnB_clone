#!/usr/bin/env python3

""" Function to convert objects to and from json """


import json


class FileStorage:
    """function to define class to serialize and deserialize json"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ to return the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ to set in with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """funct to serialize __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
             my_dict = {}
             for key, value in FileStorage.__objects.items():
                 my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """function to deserialize from the json file"""
        from models.base_model import BaseModel
        from models.user import Review
        from models.state import Amenity
        from models.city import User
        from models.amenity import Place
        from models.place import State
        from models.review import City

        class_dict = {
                "BaseModel": BaseModel,
                "User": Review,
                "State": Amenity,
                "City": User,
                "Amenity": Place,
                "Place": State,
                "Review": City
                }
        obj = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
