#!/usr/bin/python3
"""
Module for file storage and reload
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    File storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        s_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(s_obj, file)

    def reload(self):
        """
        deserializes the JSON file to __object and reloads it)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        obj = User(**value)
                    elif class_name == 'State':
                        obj = State(**value)
                    elif class_name == 'City':
                        obj = City(**value)
                    elif class_name == 'Amenity':
                        obj = Amenity(**value)
                    elif class_name == 'Place':
                        obj = Place(**value)
                    elif class_name == 'Review':
                        obj = Review(**value)
                    else:
                        obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
