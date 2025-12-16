class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or self.props == "":
            return ""
        formatted = ""
        for x in self.props:
            formatted += f" {x}={self.props[x]}"
        return formatted

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, node):
        return (
            self.tag == node.tag
            and self.value == node.value
            and self.children == node.children
            and self.props == node.props
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: No value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: No tag")
        if self.children is None:
            raise ValueError("Invalid Parent: No children")
        if self.children is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        for child in self.children:
            kiddos = "" + child.to_html()
        return f"<{self.tag}>{kiddos}</{self.tag}>"
