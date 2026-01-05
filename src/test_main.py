import unittest

from main import extract_title

class TestTextNode(unittest.TestCase):
    def test_title(self):
        self.assertEqual("Hello", extract_title("# Hello"))

    