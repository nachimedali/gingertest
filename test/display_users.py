## Loading Ginger Lib
import imp
imp.load_source("ginger", "..\lib\ginger.py")
from ginger import display_group

from mock import patch
from unittest import TestCase

class TestAnswer(TestCase):
    def test_1(self):
        with patch('__builtin__.raw_input', return_value='group3') as _raw_input:
            self.assertEqual(display_group(), 'No user with this group')
