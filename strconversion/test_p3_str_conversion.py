import unittest

from p3_str_conversion import *


class TestConverstion(unittest.TestCase):
    def test_to_str(self):
        expected = "TestingCase"
        result0 = to_str(r"TestingCase")
        result1 = to_str("TestingCase")
        self.assertEqual(expected, result0)
        self.assertEqual(expected, result1)

    def test_to_bytes(self):
        expected0 = r"TestingCase"
        result00 = to_bytes(r"TestingCase")
        result01 = to_bytes("TestingCase")
        self.assertEqual(expected0, result00)
        self.assertEqual(expected0, result01)


if __name__ == '__main__':
    unittest.main()
