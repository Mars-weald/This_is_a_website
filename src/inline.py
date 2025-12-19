from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not text_type.TEXT:
            new_nodes.append(node)
        else:
            strings = node.text.split(delimiter)
            strings[1] = delimiter + strings[1] + delimiter
            for string in strings:
                if delimiter in string:
                    non_text_node = TextNode(string, text_type)
                    new_nodes.append(non_text_node)
                else:
                    newer_nodes = TextNode(string, TextType.TEXT)
                    new_nodes.append(newer_nodes)
    return new_nodes