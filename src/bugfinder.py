from textnode import TextNode, TextType, text_node_to_html_node
from inline import *

text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
print(text_to_textnodes(text))