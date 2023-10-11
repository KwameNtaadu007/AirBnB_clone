#!/usr/bin/python3
"""File Storage for serialiazation and deserialiazation"""

import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

     # Add User to the list of classes
    _classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    obj_cls = eval(class_name)
                    obj = obj_cls(**value)
                    FileStorage.__objects[key] = obj
     
     
