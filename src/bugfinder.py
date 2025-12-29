from htmlnode import ParentNode, LeafNode

p1 = ParentNode("p", [LeafNode(None, "first")])
p2 = ParentNode("p", [LeafNode(None, "second")])
div = ParentNode("div", [p1, p2])
print(div.to_html())
