import unittest

from blocks import *

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_type_heading(self):
        block = "### Why use Flowing Claw"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_type_code(self):
        block = "``` your_function_here ```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_type_quote(self):
        block = ">This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_type_paragraph(self):
        block = "Why is anything anything blah blah blah"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)