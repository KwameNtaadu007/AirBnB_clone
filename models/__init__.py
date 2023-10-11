#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.base_model import BaseModel

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


# import other subclasses as needed

