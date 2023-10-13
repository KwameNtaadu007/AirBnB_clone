#!/usr/bin/python3

import models
from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @classmethod
    def all(cls):
        """Retrieve all instances of the User class"""
        return models.storage.all(User)

