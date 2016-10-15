## Loading Ginger Lib
import imp
imp.load_source("ginger", "../lib/ginger.py")
from ginger import find_user_mail

import unittest
from mock import patch
from unittest import TestCase

class TestAnswer(TestCase):
    def test_1(self):
        element = find_user_mail()
        self.assertEqual(element, 0)

if __name__ == '__main__':
    unittest.main()