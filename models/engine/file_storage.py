#!/usr/bin/python3
"""file_storage.py"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage():
    """create file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dictionary"""
        return self.__objects

    def new(self, obj):
        """
        the obj with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """objects to the JSON file"""
        save_obj = {}
        for k, v in self.__objects.items():
            save_obj[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as filed:
            json.dump(save_obj, filed)

    def reload(self):
        """JSON file to __objects"""
        current_classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'State': State,
            'Place': Place,
            'Review': Review
            }

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                dict_objs = json.load(file)
                for k, v in dict_objs.items():
                    cls_name = k.split('.')[0]
                    if cls_name in current_classes:
                        instance = current_classes[cls_name](**v)
                        self.new(instance)
