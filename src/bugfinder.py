from textnode import TextNode, TextType, text_node_to_html_node
print("TEST MODULE TEXTTYPE ID:", id(TextType.TEXT))

node = TextNode("This is a text node", TextType.TEXT)
html_node = text_node_to_html_node(node)
print(type(html_node))