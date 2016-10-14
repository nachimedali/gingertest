## Loading Ginger Lib
import imp
imp.load_source("ginger", "..\lib\ginger.py")
from ginger import display_user_groups

from mock import patch
from unittest import TestCase

class TestAnswer(TestCase):
    def test_1(self):
        with patch('__builtin__.raw_input', return_value='group3') as _raw_input:
            self.assertEqual(display_user_groups(), 'User mohamed ali belongs to groups group1,group2')
