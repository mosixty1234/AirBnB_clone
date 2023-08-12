#!/usr/bin/python3
"""Defines the FileStorage class"""

from models.base_model import BaseModel
import json


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

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                py_obj = json.load(f)
                for obj in py_obj.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass
