from models.base_model import BaseModel
"""
    standar documentation
"""

class Place(BaseModel):
    """
        standar documentation
        please UODATE
    """

    # |-------------------PUBLIC CLASS ATTRIBUTES-------------------|

    city_id = ""  # string - empty string: it will be the City.id
    user_id = "" # string - empty string: it will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list() #empty list: it will be the list of Amenity.id later