#!/usr/bin/python3
"""
    TEST MODULE

    in this section we approach to especif tests realized
    to all funtions in AIRBNB clone project to Holberton School
"""

import sys
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Test the amenity model class """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/amenity.py'
        result = pepstylecode.check_files([user_path])

    def setUp(self):
        self.model = Amenity()
        self.model.save()

    def test_Amenity_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
