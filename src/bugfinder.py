from textnode import TextNode, TextType, text_node_to_html_node
from blocks import *

markdown = "# This is heading"
marks = "1. Listo"
marky = "```cody showdy```"
markus = "bleh"

print(block_to_block_type(marks))
