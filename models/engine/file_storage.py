#!/usr/bin/python3
"""class that acts as file storage
for airbnb console until database
is connect"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """private properties
    __file_path: variable that stores
        file path
    __objects: objects created rom user
    """
    __file_path = 'modles/engine/file.json'
    __objects = {}

    def all(self):
        """function to return all
        objects created by baseclass
        """
        return self.__objects

    def new(self, obj):
        """method to create new object
        in file storage"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """method to save file in json
        data format"""
        jsonData = {}
        for key, value in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonData, f)

    def reload(self):
        """method to open data saved by json"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    newObj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = newObj
        except FileNotFoundError:
            pass
