#!/usr/bin/python3
"""user class that holds basic info
of the user"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class atributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
