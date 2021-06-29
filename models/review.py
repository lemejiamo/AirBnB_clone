#!/usr/bin/python3
"""
   Class Review to AirBnB clone
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review inherits from class BaseModel
    """
    # |-------------------PUBLIC CLASS ATTRIBUTES-------------------|

    place_id = ""  # empty string: it will be the Place.id
    user_id = ""  # empty string: it will be the User.id
    text = ""  # empty string
