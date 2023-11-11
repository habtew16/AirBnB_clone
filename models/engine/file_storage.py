#!/usr/bin/python3
"""class that acts as file storage
for airbnb console until database
is connect"""
import json
from models.base_model import BaseModel

class FileStorage:
    """private properties"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
    def save(self):
        jsonData = {}
        for key, value in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonData, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    newObj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = newObj
        except FileNotFoundError:
            pass

