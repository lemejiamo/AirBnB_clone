#!/usr/bin/python3
"""
    class User to AirBNB clone project from Holberton School
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        class User inherits from BaseModel

        PUBLIC CLASS ATTRIBUTES:
            email:string
            password:string
            firts_name:string
            last_name:string
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """
            CONSTRUCTOR
        """
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            self.first_name = ""
            self.last_name = ""
            self.email = ""
            self.password = ""

# |------------OVERRIDE __STR__ METHOD-----------|
    def __str__(self):
        """
            Print the string representation of instance
        """

        return ("[{}] ({}) {}".format(
                __class__.__name__,
                self.id,
                self.__dict__))
