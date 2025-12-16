import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
