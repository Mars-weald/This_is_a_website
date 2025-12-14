import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("<p>", "paragraph", None, None)
        node2 = HTMLNode("<p>", "paragraph", None, None)
        self.assertEqual(node1, node2)

    def test_tag_not_eq(self):
        node1 = HTMLNode("<h1>", "heading", ["child"], {"href": "https://www.tmbw.net", "target": "_blank"})
        node2 = HTMLNode("<p>", "heading", ["child"], {"href": "https://www.tmbw.net", "target": "_blank"})
        self.assertNotEqual(node1, node2)

    def test_child_not_eq(self):
        node1 = HTMLNode("<h1>", "heading", ["child"], {"href": "https://www.tmbw.net", "target": "_blank"})
        node2 = HTMLNode("<h1>", "heading", None, {"href": "https://www.tmbw.net", "target": "_blank"})
        self.assertNotEqual(node1, node2)

    def test_props_not_eq(self):
        node1 = HTMLNode("<h1>", "heading", ["child"], {"href": "https://www.tmbw.net", "target": "_blank"})
        node2 = HTMLNode("<h1>", "heading", ["child"], {"href": "https://www.tmbw.net", "target": "_bank"})
        self.assertNotEqual(node1, node2)