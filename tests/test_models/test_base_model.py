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
        model_dict = {'name': 'holberton', 'edad': 23}

        test_model = BaseModel()
        test_model.name = "holberton"
        test_model.edad = 23
        print(test_model)

        # test to verify the instance
        self.assertIsInstance(test_model, BaseModel)

        # test to verify the type of variable

        self.assertEqual(type(test_model.created_at), datetime)

        self.assertEqual(type(test_model.update_at), datetime)

        self.assertEqual(type(test_model.id), str)

        self.assertEqual(type(test_model.name), str)

        # test to verify the  assigment of var
        self.assertEqual(test_model.name, "holberton")

        self.assertEqual(test_model.edad, 23)

        self.assertTrue(test_model.id)

        update_pre = test_model.update_at
        test_model.save()
        self.assertTrue(test_model.update_at > update_pre)

        # test to verify if KWARGS contains something
        test_model2 = BaseModel(**model_dict)
        self.assertEqual(test_model2.name, 'holberton')
        self.assertEqual(test_model2.edad, 23)

if __name__ == "__main__":
    unittest.main()
