from main import *

with open("content/blog/majesty/index.md") as f:
    md = f.read()

node = markdown_to_html_node(md)
print(node.to_html())
