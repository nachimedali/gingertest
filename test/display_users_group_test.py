## Loading Ginger Lib
import imp
imp.load_source("ginger", "../lib/ginger.py")
from ginger import display_user_groups
data_file="../data/address_book_file.json"
import unittest
from mock import patch
from unittest import TestCase

class TestAnswer(TestCase):
    def test_1(self):
        element = display_user_groups()
        self.assertEqual(element, 0)

if __name__ == '__main__':
    unittest.main()