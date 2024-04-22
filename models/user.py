#!usr/bin/python3
"""usr.py"""
from models.base_model import BaseModel


class User(BaseModel):
    """create user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
