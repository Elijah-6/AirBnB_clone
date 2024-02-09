#!/usr/bin/env python
"""Defines a base model."""

import uuid
from datetime import datetime

class BaseModel:
    """
        BaseModel class defines common attributes and methods for other classes.

        Public instance attributes:
            id: str - Assigned with a unique UUID when an instance is created.
            created_at: datetime - Assigned with the current datetime when an instance is created.
            updated_at: datetime - Assigned with the current datetime when an instance is created and
                                updated every time the object is changed.

        Public instance methods:
            __init__(): Initializes the BaseModel instance.
            __str__(): Returns a string representation of the instance.
            save(): Updates the public instance attribute 'updated_at' with the current datetime.
            to_dict(): Returns a dictionary containing all keys/values of __dict__ of the instance.
    """
    def __init__(self, *args, **kwargs):
        """
            Initializes a new instance of the BaseModel class.

            Attributes:
                id (str): Unique identifier generated using uuid.uuid4().
                created_at (datetime): Current datetime when the instance is created.
                updated_at (datetime): Current datetime when the instance is created and updated during modifications.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            Returns a string representation of the BaseModel instance.

            Returns:
                str: A formatted string containing the class name, id, and __dict__.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance attribute 'updated_at' with the current datetime.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns a dictionary representation of the instance.

            Returns:
                dict: A dictionary containing all keys/values of __dict__ and additional metadata.
                  Keys include '__class__', 'created_at', and 'updated_at'.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
