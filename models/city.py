#!/usr/bin/python3
"""city class module"""
from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initializes City instance"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
