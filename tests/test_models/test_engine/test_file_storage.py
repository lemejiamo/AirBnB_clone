#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""
    TEST MODULE

    in this section we approach to especif tests realized
    to all funtions in AIRBNB clone project to Holberton School
"""
from models.base_model import BaseModel
import unittest
import os


class Test_file_storage(unittest.TestCase):
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
        base_type_name = type(test_model.name)
        print(type(test_model.name))
        self.assertEqual(base_type_name, str)

        base_type_create = type(test_model.created_at)
        print(base_type_create)
        self.assertEqual(type(test_model.created_at), base_type_create)

        base_type_update = type(test_model.update_at)
        self.assertEqual(type(test_model.update_at), base_type_update)

        baase_type_id = type(test_model.id)
        self.assertEqual(type(test_model.id), str)

        # test to verify if KWARGS contains something

        test_model2 = BaseModel(**model_dict)
        self.assertEqual(test_model2.name, 'holberton')

        with self.assertRaises(TypeError):
            BaseModel(2)

        test_list = list()
        with self.assertRaises(TypeError):
            BaseModel(test_list)

    def test_str_method(self):
        """
            Test to verify the print of magic __str__ method
        """
        model_dict = {'name': 'holberton', 'edad': '23', 'id': '0'}
        test_model = BaseModel(**model_dict)

        print(test_model)

        pass

    def test_save(self):

        # Test to check update function
        model_dict = {'name': 'holberton', 'edad': '23', 'id': '0'}
        test_model = BaseModel(**model_dict)
        test_model.save()
        self.assertNotEqual(test_model.created_at, test_model.update_at)

    def test_to_dict_method(self):
        """
            Test to verify to_dict_method
        """
        # comprobar si la salida es diferente
        # comprobar el formato de salida de la fecha debe ser STR

        pass

    def test_to_kwargs(self):
        # verificar que le valor de kwargs sea cero cuando no se pase nada
        pass

    def test_to_storage(self):
        # verify
        pass

    def test_save_storage(self):
        # verificar que las listas no sean nulas o vacias
        pass

    def test_reload(self):
        # verificar si el archivo existe
        pass

# |------------ENTRY POINT------------|


if __name__ == "__main__":
    unittest.main()
