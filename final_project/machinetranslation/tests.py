"""
    This module implements Unit Test of translator module
"""
import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrenchTranslation(unittest.TestCase):
    def test_e2f_null_input(self):
        # 1. Input none
        input_text = None
        expected_text = ""
        output_text = english_to_french(input_text)
        self.assertEqual(output_text, expected_text)
        # 2. Input null string
        input_text = ""
        expected_text = ""
        output_text = english_to_french(input_text)
        self.assertEqual(output_text, expected_text)

class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_f2e_null_input(self):
        # 1. Input none
        input_text = None
        expected_text = ""
        output_text = french_to_english(input_text)
        self.assertEqual(output_text, expected_text)
        # 2. Input null string
        input_text = ""
        expected_text = ""
        output_text = french_to_english(input_text)
        self.assertEqual(output_text, expected_text)

if __name__ == '__main__':
    unittest.main()