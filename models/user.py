#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Handles serialization and deserialization of objects to/from JSON file"""

    # Existing methods and attributes

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
                    obj = obj_cls(**obj_data)
                    self.__objects[obj_id] = obj
        except FileNotFoundError:
            pass

