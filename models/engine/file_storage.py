#!/usr/bin/python3
"""Defines the FileStorage class"""

from models.base_model import BaseModel
import json
import os
from models.user import User


class FileStorage:
    """
    Represents a storage engine

    Attributes:
        __file_path (str): The name of the file to save objects to
        __objects (dict): A dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns  __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = FileStorage.__objects
        py_obj = {key: value.to_dict() for key, value in obj_dict.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(py_obj, f)
        
        def classes(self):
        """This returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                py_obj = json.load(f)
                for obj in py_obj.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))

         def attributes(self):
        """This returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return  attributes
        except FileNotFoundError:
            pass

