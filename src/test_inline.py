import unittest

from textnode import TextNode, TextType
from inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

class TestTextNode(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]
        self.assertEqual(new_nodes, result)

    def test_bold_block(self):
        node = TextNode("This is text with **bolded words** here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [TextNode("This is text with ", TextType.TEXT), TextNode("bolded words", TextType.BOLD), TextNode(" here", TextType.TEXT)]
        self.assertEqual(new_nodes, result)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_again(self):
        matches = extract_markdown_images("This has TWO ![image](https://homestarrunner.net) ![s](https://homestarrunner.communism)")
        self.assertListEqual([("image", "https://homestarrunner.net"), ("s", "https://homestarrunner.communism")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_links_again(self):
        matches = extract_markdown_links("This has a link [to homestar](https://homestarrunner.com/)")
        self.assertListEqual([("to homestar", "https://homestarrunner.com/")], matches)

    
    def test_split_links(self):
        node = TextNode("This is a node with a link [to homestar](https://homestarrunner.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a node with a link ", TextType.TEXT), 
                TextNode("to homestar", TextType.LINK, "https://homestarrunner.com")
            ], new_nodes
        )

    def test_split_link_text_after(self):
        node = TextNode("This is a node with a link [to homestar](https://homestarrunner.com) and some text after", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a node with a link ", TextType.TEXT),
                TextNode("to homestar", TextType.LINK, "https://homestarrunner.com"),
                TextNode(" and some text after", TextType.TEXT)
            ], new_nodes
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], result
        )