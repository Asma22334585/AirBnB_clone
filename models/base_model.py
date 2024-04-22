#!/usr/bin/python3
"""base_model.py"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """initalisation of an object"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
                elif k in ('created_at', 'updated_at'):
                    Newv = datetime.fromisoformat(v)
                    setattr(self, k, Newv)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """str of instences"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        if isinstance(self.created_at, datetime):
            dict['created_at'] = self.created_at.isoformat()
        else:
            dict['created_at'] = self.created_at
        if isinstance(self.updated_at, datetime):
            dict['updated_at'] = self.updated_at.isoformat()
        else:
            dict['updated_at'] = self.updated_at
        return dict
