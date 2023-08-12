#!/usr/bin/python3
"""Defines the FileStorage class"""

from models.base_model import BaseModel
import json
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
        

        def __init__(self):
        """Initializes FileStorage instance"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        if cls is None:
            return self.__objects
        else:
            cls_name = cls.__name__
            cls_objects = {}
            for obj_id, obj in self.__objects.items():
                if cls_name in obj_id:
                    cls_objects[obj_id] = obj
            return cls_objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary"""
        self.__objects[obj.id] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        serialized_objs = {}
        for obj_id, obj in self.__objects.items():
            serialized_objs[obj_id] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                deserialized_objs = json.load(file)
                for obj_id, obj_data in deserialized_objs.items():
                    class_name = obj_data["__class__"]
                    obj_cls = globals()[class_name]
                    if obj_cls == User:  # Check if the class is User
                        obj = User(**obj_data)
                    else:
                        obj = obj_cls(**obj_data)
                    self.__objects[obj_id] = obj
        except FileNotFoundError: 
             pass
