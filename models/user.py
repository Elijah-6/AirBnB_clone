#!/usr/bin/python3

"""User class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that defines a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a user
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get("email", '')
        self.password = kwargs.get("password", '')
        self.first_name = kwargs.get("first_name", '')
        self.last_name = kwargs.get("last_name", '')
