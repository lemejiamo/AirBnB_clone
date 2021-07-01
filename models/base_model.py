#!/usr/bin/python3

"""
    Project AIRBNB clone for Holberton School
"""

import copy
import models
from uuid import uuid4
from datetime import datetime



class BaseModel():
    """
        Super Class for AIRBNB project

        PUBLIC INSTANCE METHODS:

            save(self): updates the public instance attribute
                        updated_at with the current datetime

            to_dict(self): returns a dictionary containing all keys/values
                           of __dict__ of the instance a key __class__ be added

        PUBLIC INSTANCE ATTRIBUTES:

            id:int assign with an uuid when an instance is created
            create_at:datetime
            update_at:datetime
    """

# |-------------------CONSTRUCTOR-------------------|
    def __init__(self, *args, **kwargs):
        """
            CONSTRUCTOR FOR BASE MODEL
        """
        self.id = str(uuid4())
        time = datetime.now()
        self.created_at = time
        self.update_at = time

        if kwargs:
            for key in kwargs.keys():
                if key == "created_at":
                    time = datetime.strptime(
                        kwargs.get(key),
                        "%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = time
                elif key == "update_at":
                    time = datetime.strptime(
                        kwargs.get(key),
                        "%Y-%m-%dT%H:%M:%S.%f")
                    self.update_at = time
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            time = datetime.now()
            self.created_at = time
            self.update_at = time

        models.storage.new(self)

# |--------------SETTER & GETTER 'name'-----------|
    @property
    def _name(self):
        """
            Getter for name value
        """

        return (self.name)

    @_name.setter
    def _name(self, name):
        """
            Setter from name value
        """
        if type(name) is not str:
            raise TypeError
        self.name = name

# |-----------PRIVATE INSTANCE METHODS-----------|
# |------------OVERRIDE __STR__ METHOD-----------|
    def __str__(self):
        """
            Print the string representation of instance
        """

        return ("[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__))

# |----------- END PRIVATE METHODS -------------|

# |---------PUBLIC INSTANCE METHODS ------------|

    def save(self):
        """
             updates the public instance attribute
             'updated_at' with the current datetime
        """

        time = datetime.now()
        self.update_at = time
        #models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """

        dictionary = copy.deepcopy(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = datetime.isoformat(self.created_at)
        dictionary['update_at'] = datetime.isoformat(self.update_at)
        return dictionary
