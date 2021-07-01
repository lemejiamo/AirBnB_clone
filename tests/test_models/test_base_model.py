#!/usr/bin/python3
"""
    TEST MODULE

    in this section we approach to especif tests realized
    to all funtions in AIRBNB clone project to Holberton School
"""
import unittest
import re
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """
        Superclass from all foward tests
    """

    def test_CONSTRUCTOR(self):
        """
            test to CONSTRUCTOR (__init__)
            in class base_model
        """
        model_dict = {'name': 'holberton', 'edad': '23'}

        test_model = BaseModel(**model_dict)

        # test to verify the instance
        self.assertIsInstance(test_model, BaseModel)

        # test to verify the type of variable

        self.assertEqual(type(test_model.created_at), datetime)

        self.assertEqual(type(test_model.update_at), datetime)

        self.assertEqual(type(test_model.id), str)

        self.assertEqual(type(test_model.name), str)

        # test to verify the  assigment of var
        self.assertEqual(test_model.name, "Holberton")

        self.assertEqual(test_model.edad, 23)

        self.assertTrue(test_model.id)

        updated_pre = test_model.updated_at
        test_model.save()
        self.assertTrue(test_model.updated_at > updated_pre)

        # test to verify if KWARGS contains something
        test_model2 = BaseModel(**model_dict)
        self.assertEqual(test_model2.name, 'holberton')
        self.assertEqual(test_model2.edad, 23)

    def test_str(self):
        '''[check __str__ method]'''
        my_model = BaseModel()
        r = re.compile("[BaseModel] (.*) {.*}")
        my_str = my_model.__str__()
        self.assertIsNotNone(r.match(my_str))


if __name__ == "__main__":
    unittest.main()
