## Loading Ginger Lib
import imp
imp.load_source("ginger", "..\lib\ginger.py")
from ginger import add_group

from mock import patch
from unittest import TestCase

class TestAnswer(TestCase):
    def test_1(self):
        with patch('__builtin__.raw_input', return_value='group2') as _raw_input:
            self.assertEqual(add_group(), 'Group group2 already in list')

    def test_2(self):
        with patch('__builtin__.raw_input', return_value='group4') as _raw_input:
            self.assertEqual(answer(), 'Group added')
