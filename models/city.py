#!/usr/bin/python3
"""city class to inherit from basemodel"""
from models.base_model import BaseModel

class City(BaseModel):
    """stateid and name attribue of city"""
    state_id = ""
    name = ""
