import unittest

from calculator_string import adddtion_of_string_values

class TestStringCalculator(unittest.TestCase):

  def test_empty_string(self):
    self.assertEqual(adddtion_of_string_values(""), 0)

  def test_comma(self):
    self.assertEqual(adddtion_of_string_values("4"), 4)
    self.assertEqual(adddtion_of_string_values("4,5"), 9)

  def test_newlines(self):
    self.assertEqual(adddtion_of_string_values("3\n5,1"), 9)
    self.assertRaises(ValueError, adddtion_of_string_values, "1,\n")

  def test_delimeter(self):
    self.assertEqual(adddtion_of_string_values("//;\n1;4;2;3"), 10)
    self.assertEqual(adddtion_of_string_values("//*\n1*4*2*3"), 10)
    self.assertRaises(ValueError, adddtion_of_string_values, "//*\n1*\n")

  def test_negatives(self):
    self.assertRaises(ValueError, adddtion_of_string_values ,"1,-3")
