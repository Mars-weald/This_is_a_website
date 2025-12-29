from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        strings = node.text.split(delimiter)
        if len(strings) % 2 == 0:
            raise Exception("ERROR: Unmatched Delimiter")
        for i, string in enumerate(strings):
            if string == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(string, TextType.TEXT))
            else:
                new_nodes.append(TextNode(string, text_type))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    end_list = []
    for node in old_nodes:
        node_copy = node
        if node.text == "":
            continue
        if node.text_type != TextType.TEXT:
            end_list.append(node)
            continue
        matches = extract_markdown_images(node_copy.text)
        if len(matches) == 0:
            end_list.append(node)
            continue
        for match in matches:
            alt, url = match
            splitter = node_copy.text.split(f"![{alt}]({url})", 1)
            if len(splitter) != 2:
                raise ValueError("ERROR: Invalid image syntax")
            if splitter[0] != "":
                end_list.append(TextNode(splitter[0], TextType.TEXT))
            end_list.append(TextNode(alt, TextType.IMAGE, url))
            node_copy = TextNode(splitter[1], TextType.TEXT)
            if node_copy.text != "":
                end_list.append(TextNode(node_copy.text, TextType.TEXT))
    return end_list           

def split_nodes_link(old_nodes):
    end_list = []
    for node in old_nodes:
        node_copy = node
        if node.text == "":
            continue
        if node_copy.text_type != TextType.TEXT:
            end_list.append(node)
            continue
        matches  = extract_markdown_links(node_copy.text)
        if len(matches) == 0:
            end_list.append(node)
            continue
        for match in matches:
            alt, url = match
            splitter = node_copy.text.split(f"[{alt}]({url})", 1)
            if len(splitter) != 2:
                raise ValueError("ERROR: Invalid link syntax")
            if splitter[0] != "":
                end_list.append(TextNode(splitter[0], TextType.TEXT))
            end_list.append(TextNode(alt, TextType.LINK, url))
            node_copy = TextNode(splitter[1], TextType.TEXT)
        if node_copy.text != "":
            end_list.append(node_copy)
    return end_list


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes