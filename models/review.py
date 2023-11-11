#!/usr/bin/python3
"""review class to inherit from basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """attributes of review class"""
    place_id = ""
    user_id = ""
    text = ""
