#!/usr/bin/python3
from models.base_model import BaseModel
"""
   Class Place to AirBnB clone
"""


class Place(BaseModel):
    """
        Place inherits from class BaseModel
    """

    # |-------------------PUBLIC CLASS ATTRIBUTES-------------------|

    city_id = ""  # string - empty string: it will be the City.id
    user_id = ""  # string - empty string: it will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list()  # empty list: it will be the list of Amenity.id later
