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

    def test_e2f(self):
        # 1. Test Hello translated to Bonjour
        input_text = "Hello"
        expected_text = "Bonjour"
        output_text = english_to_french(input_text)
        self.assertEqual(output_text, expected_text)
        # 2. Test Hello does not return Hello
        input_text = "Hello"
        output_text = english_to_french(input_text)
        self.assertNotEqual(output_text, input_text)



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

    def test_f2e(self):
        # 1. Test Bonjour translated to Hello
        input_text = "Bonjour"
        expected_text = "Hello"
        output_text = french_to_english(input_text)
        self.assertEqual(output_text, expected_text)
        # 2. Test Bonjour does not return Bonjour
        input_text = "Bonjour"
        output_text = french_to_english(input_text)
        self.assertNotEqual(output_text, input_text)


if __name__ == '__main__':
    unittest.main()