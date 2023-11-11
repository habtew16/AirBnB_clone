#!/usr/bin/python3
"""base class for the airbnb console
project from which all the other class
inherit and based on"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """base model class for the airbnb poject"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            args: Non-keyword arguments
            kwargs: Key-value arguments for instantiation
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string function that changes string of
        the base_models that is returned when it is
        instantiated"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """this is function to return string of
        the class BaseModel"""
        return self.__str__()

    def save(self):
        """public function to update time
        and to save class to the filestorage
        of the console project"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """method to convert class to dictionary"""
        obj = self.__dict__.copy()
        obj['__class__'] = str(self.__class__.__name__)
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
