#!/usr/bin/python3
"""
    Module to storing data and load from JSON file
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City


class FileStorage():
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances

        Private class attributes:
            __file_path:string - path to the JSON file
            to store de data

            __objects:dictionary - empty but will store
            all objects by <class name>.id (ex: to store
            a BaseModel object with id=12121212, the key
            will be BaseModel.12121212)

    """

    # |---------------PRIVATE CLASS ATTRIBUTES---------------|
    __file_path = "data.json"
    __objects = {}

    # |--------------SETTER & GETTER 'name'-----------|
    @property
    def objects(self):
        """
            Getter for objects
        """

        return (self.__objects)

    # |---------------PUBLIC INSTANCE METHODS ---------------|
    def all(self):
        """
            returns the dictionary of all objects
        """
        all_objects = dict()
        for key in self.__objects:
            instance_dict = self.objects.get(key)
            instance_object = eval(instance_dict.get('__class__'))(**instance_dict)
            all_objects[key] = (instance_object.__str__())

        return (all_objects)

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id

            Attributes:
            Obj: object to add to the __objects dict
        """

        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        dictionary = (obj.to_dict())
        self.__objects[key] = dictionary

    def save(self):
        """
            serializes __objects to the JSON file
            (path: __file_path)
        """

        dump = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as storage_file:
            storage_file.write(dump)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as read_file:
                self.__objects = json.load(read_file)
                self.all()
        except FileNotFoundError:
            pass
