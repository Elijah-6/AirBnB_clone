#!/usr/bin/env python
"""Defines a base model."""

import uuid
from datetime import datetime


class BaseModel:
    """
        BaseModel class defines common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Initializes a new instance of the BaseModel class.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            Updates the public instance attribute 'updated_at'
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns a dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
